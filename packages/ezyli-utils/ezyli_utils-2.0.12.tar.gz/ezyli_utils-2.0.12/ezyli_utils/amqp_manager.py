import pika
import time
import json
from pika.exchange_type import ExchangeType
from pika.exceptions import ChannelClosed, AMQPConnectionError
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from .validator import validate_data
from .schemas import COMMON_SCHEMA


def construct_url(
    url,
    heartbeat=None,
    connection_attempts=None,
    retry_delay=None,
):
    """
    Heartbeats: RabbitMQ uses a heartbeat mechanism to detect if a client is still alive.
    If the client doesn't send any data for a certain period of time (the heartbeat interval),
    RabbitMQ will close the connection. You should ensure that your client sends data
    frequently enough to keep the connection alive.

    > The url_parts[4] refers to the query component of the URL.
    When you parse a URL using urlparse, it returns a 6-tuple
    containing the following components: scheme, netloc, path, params, query, and fragment.
    The query component is at index 4.
    """
    url_parts = list(urlparse(url))
    query = dict(parse_qs(url_parts[4]))
    if heartbeat is not None:
        query.update({"heartbeat": heartbeat})
    if connection_attempts is not None:
        query.update({"connection_attempts": connection_attempts})
    if retry_delay is not None:
        query.update({"retry_delay": retry_delay})

    url_parts[4] = urlencode(query)

    return urlunparse(url_parts)


class AMQPManager:
    """
    >> The lock is used to ensure thread safety. In multi-threaded environments,
     it's possible for multiple threads to access and modify shared data simultaneously.
     This can lead to inconsistent state and hard-to-debug issues.
     The lock object is a synchronization primitive that can be used to ensure that
     only one thread can enter a particular section of code at a time. In the context
     of the `AMQPHandler` class, the lock is used to ensure that only one thread
     can use the `channel` object at a time, preventing potential race conditions.
    """

    def __init__(
        self,
        url,
        heartbeat=None,
        connection_attempts=None,
        retry_delay=None,
        use_singleton=True,
    ):
        print("AMQPManager :: __init__")
        url = construct_url(
            url=url,
            heartbeat=heartbeat,
            connection_attempts=connection_attempts,
            retry_delay=retry_delay,
        )
        # url = url
        print(f"AMQP URL: {url}")
        self.params = pika.URLParameters(url)
        self.connection = None
        self.channel = None
        self.connect_counter = 0

    def connect(self, retry=True):
        self._connect(retry=retry)

    def publish(
        self,
        routing_key,
        message,
        exchange_name="",  # Default exchange
        content_type=None,
        max_retries=5,
        delivery_mode=2,
        headers=None,
    ):
        self._publish(
            routing_key=routing_key,
            message=message,
            exchange_name=exchange_name,
            content_type=content_type,
            max_retries=max_retries,
            delivery_mode=delivery_mode,
            headers=headers,
        )

    def consume(
        self,
        queue,
        callback,
        validate_common_schema=False,
        auto_ack=True,
    ):
        self._consume(
            queue=queue,
            callback=callback,
            validate_common_schema=validate_common_schema,
            auto_ack=auto_ack,
        )

    def _exchange_declare(
        self, exchange_name, exchange_type: ExchangeType, durable=False
    ):
        self.channel.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type,
            durable=durable,
        )
        print(f"Exchange {exchange_name} declared")

    def exchange_declare(
        self,
        exchange_name,
        exchange_type: ExchangeType,
        durable=False,
        wait_for_conn=False,
        max_retries=5,
        retry_delay=5,
    ):
        for _ in range(max_retries):
            try:
                if self.channel is None or self.channel.is_closed:
                    self.connect(retry=wait_for_conn)
                self._exchange_declare(exchange_name, exchange_type, durable)
                break  # If the declaration was successful, break the loop
            except Exception as e:
                print(f"An error occurred when trying to declare exchange: {e}")
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)  # Wait for retry_delay seconds before retrying

    def _queue_declare(self, queue_name, durable=False):
        self.channel.queue_declare(queue=queue_name, durable=durable)
        print(f"Queue {queue_name} declared")

    def queue_declare(self, queue_name, durable=False, wait_for_conn=False):
        try:
            if self.channel is None or self.channel.is_closed:
                self.connect(retry=wait_for_conn)
            self._queue_declare(queue_name, durable)
        except Exception as e:
            print(f"An error occurred when trying to declare queue: {e}")

    def _queue_bind(
        self,
        queue_name,
        exchange_name,
        routing_key,
        arguments=None,
    ):
        self.channel.queue_bind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=routing_key,
            arguments=arguments,
        )
        print(f"Queue {queue_name} bound to exchange {exchange_name}")

    def queue_bind(
        self,
        queue_name,
        exchange_name,
        routing_key,
        wait_for_conn=False,
        max_retries=5,
        arguments=None,
    ):
        for _ in range(max_retries):
            try:
                if self.channel is None or self.channel.is_closed:
                    self.connect(retry=wait_for_conn)
                self._queue_bind(
                    queue_name,
                    exchange_name,
                    routing_key,
                    arguments=arguments,
                )
                break  # If the binding was successful, break the loop
            except Exception as e:
                print(f"An error occurred when trying to bind queue: {e}")

    def _queue_unbind(self, queue_name, exchange_name, routing_key):
        self.channel.queue_unbind(
            exchange=exchange_name,
            queue=queue_name,
            routing_key=routing_key,
        )
        print(f"Queue {queue_name} unbound from exchange {exchange_name}")

    def queue_unbind(self, queue_name, exchange_name, routing_key, wait_for_conn=False):
        try:
            if self.channel is None or self.channel.is_closed:
                self.connect(retry=wait_for_conn)
            self._queue_unbind(queue_name, exchange_name, routing_key)
        except Exception as e:
            print(f"An error occurred when trying to unbind queue: {e}")

    def _connect(self, retry=True):
        while True:
            self.connect_counter += 1
            try:
                if self.connection and self.connection.is_open:
                    self.channel = self.connection.channel()
                    break
                self.close()
                self.connection = pika.BlockingConnection(self.params)
                self.channel = self.connection.channel()
                # Reset the counter if the connection is successful
                self.connect_counter = 0
                break  # If the connection is successful, break the loop
            except pika.exceptions.AMQPConnectionError as e:
                if not retry:
                    raise
                print(f"An error occurred when trying to connect: {e}")
                time.sleep(5) if self.connect_counter > 1 else time.sleep(0)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break

    def _publish(
        self,
        routing_key,
        message,
        exchange_name="",  # Default exchange
        content_type=None,
        max_retries=5,
        delivery_mode=2,
        headers=None,
    ):
        """
        # delivery_mode=2 make message persistent
        """
        retries = 0
        while retries <= max_retries:
            try:
                if self.channel is None or self.channel.is_closed:
                    self.connect(retry=False)
                    if self.channel is None:
                        raise Exception("Failed to establish connection")
                self.channel.basic_publish(
                    exchange=exchange_name,
                    routing_key=routing_key,
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=delivery_mode,
                        content_type=content_type,
                        headers=headers,
                    ),
                )
                print(
                    f"Published message to {exchange_name} with routing key {routing_key}"
                )
                break  # If the operation is successful, break the loop
            except (
                pika.exceptions.ChannelClosed,
                pika.exceptions.AMQPConnectionError,
                Exception,
            ) as e:
                print(f"Error occurred: {e}, retrying...")
                retries += 1
                if retries > max_retries:
                    raise  # If max retries reached, re-raise the last exception
                # Wait before retrying
                time.sleep(5)
                self.connect(retry=False)

    def _consume(
        self,
        queue,
        callback,
        validate_common_schema=False,
        auto_ack=True,
    ):
        def internal_callback(ch, method, properties, body):
            if not validate_common_schema or self._is_valid_body(body):
                callback(ch, method, properties, body)

        while True:
            print("Setting up consumer :- ...")
            if self.channel is None or self.channel.is_closed:
                self.connect()
            try:
                self.channel.basic_consume(
                    queue=queue,
                    on_message_callback=internal_callback,
                    auto_ack=auto_ack,
                )

                print("Started Consuming...")

                self.channel.start_consuming()
            except (
                pika.exceptions.ChannelClosed,
                pika.exceptions.AMQPConnectionError,
            ) as e:
                print("Reconnecting ...")
                self.reconnect()
            except Exception as e:
                print("Reconnecting ...")
                print(e)
                self.reconnect()

    def close(self):
        try:
            if self.channel is not None:
                self.channel.close()
            if self.connection is not None:
                self.connection.close()
        except Exception as e:
            print(f"An error occurred when trying to close the connection: {e}")

    def reconnect(self):
        self.connect()

    def validate_data(self, data, schema):
        return validate_data(data, schema)

    def _is_valid_body(self, body):
        # Convert body from bytes to string and then to a dictionary
        try:
            content = json.loads(body.decode())
        except json.JSONDecodeError:
            print(f"Invalid JSON received :: {body.decode()}")
            return False
        schema = COMMON_SCHEMA
        return self.validate_data(content, schema)
