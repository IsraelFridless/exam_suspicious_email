import os

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

load_dotenv(verbose=True)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])
    topic_names = [
        os.environ['TOPIC_ALL_MESSAGES_NAME'],
    ]
    topics = [
        NewTopic(
            name=topic_name,
            num_partitions=int(os.environ['NUM_PARTITIONS']),
            replication_factor=int(os.environ['REPLICATION_FACTOR'])
        )
        for topic_name in topic_names
    ]
    try:
        client.create_topics(topics)
    except TopicAlreadyExistsError as e:
        print(str(e))
    finally:
        client.close()


if __name__ == '__main__':
    init_topics()