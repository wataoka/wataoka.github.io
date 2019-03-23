class Work:
    def __init__(self, id, name, image="", description="", qiita="", github=""):
        self.id = id
        self.name = name
        self.image = "images/" + image
        self.description = description
        self.qiita = qiita
        self.github = github