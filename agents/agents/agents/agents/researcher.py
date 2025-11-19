class Researcher:
    def generate_literature(self, topic):
        # PRO VERSION: Mocked structured literature (for offline reproducibility)
        papers = [
            {
                "title": "Foundational Approaches to " + topic,
                "summary": "This paper explains core ideas related to " + topic,
                "url": "https://example.com/1"
            },
            {
                "title": "Modern ML Techniques for " + topic,
                "summary": "Discusses recent state-of-the-art techniques.",
                "url": "https://example.com/2"
            }
        ]
        return papers
