from elasticsearch import Elasticsearch


def add_basic_es_arguments(parser):
    group = parser.add_argument_group('Elasticsearch')
    group.add('--es-host', '-o', required=True, dest='es_host',
              help='Elasticsearch host', env_var='ES_HOST')
    group.add('--es-port', '-p', dest='es_port', default='9200',
              help='Elasticsearch port', env_var='ES_PORT')
    group.add('--es-username', '-u', dest='es_username',
              default='',
              help='Elasticsearch username', env_var='ES_USERNAME')
    group.add('--es-password', '-a', dest='es_password',
              default='',
              help='Elasticsearch password', env_var='ES_PASSWORD')
    group.add('--index-name',  dest='index_name', required=True,
              help='Elasticsearch index name')
    return group


def get_es_connection(config):
    url = "{}://{}:{}".format("http", config.es_host, config.es_port)
    es = Elasticsearch(
        url, http_auth=(config.es_username, config.es_password),
        user_ssl=True, timeout=1000
    )
    return es


__all__ = ['add_basic_es_arguments', 'get_es_connection']
