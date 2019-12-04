import enum

from model.artifact_pkg.artifact import Artifact


class Paper(Artifact):
    class ArtifactType(enum.Enum):
        PAPER = "Paper"
        REVIEW = "Review"
        REPORT = "Report"

    def __init__(self, artifact_id: int, corresponding_id: int, artifact_type: ArtifactType, author_id: int,
                 artifact_name: str, title: str, authors: str, version: int, topic: str):
        super().__init__(artifact_id, corresponding_id, artifact_type, author_id, artifact_name)
        self._title = title
        self._authors = authors
        self._version = version
        self._topic = topic

    def create_artifact_hash(self):
        return {"artifactID": self.artifact_id,
                "correspondingID": self._corresponding_id,
                "type": self._artifact_type.value,
                "authorID": self._author_id,
                "artifactName": self.artifact_name,
                "title": self._title,
                "authors": self._authors,
                "version": self._version,
                "topic": self._topic
                }


# a = Paper(1, 1, Artifact.ArtifactType.PAPER, 1, 'a', 'a', 'a', 1, 'a')
# print(a.artifact_id)