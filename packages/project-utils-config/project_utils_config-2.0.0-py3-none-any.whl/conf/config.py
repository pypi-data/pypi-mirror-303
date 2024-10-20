from project_utils.conf import BaseConfig


class Config(BaseConfig):

    def config_init(self):
        self.config_object.load_elasticsearch(**self.parser['ELASTICSEARCH'])
        self.config_object.load_faiss(**self.parser['FAISS'])
        self.config_object.load_ftp(**self.parser['FTP'])
        self.config_object.load_graph(**self.parser['GRAPH'])
