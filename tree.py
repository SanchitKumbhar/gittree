from streamlit_agraph import agraph, Node, Edge, Config
from main import Main



class NonMergeCommitTree(Main):
    nodes = []
    edges = []

    node_ids = set()
    edge_pairs = set()

    # Add main branch node
    nodes.append(Node(id="main", label="main", size=25))
    node_ids.add("main")
# Normal commits
    def normal_commit_tree(self,branch):
            if branch == "main":
                self.main_branch()
            else:
                 self.user_branch()
            for i in reversed(self.normal_commits):
                commit_id = i.get("id")
                if commit_id not in self.node_ids:
                    self.nodes.append(Node(id=commit_id, label=i.get("message"), size=25))
                    self.node_ids.add(commit_id)
                if ("main", commit_id) not in self.edge_pairs:
                    self.edges.append(Edge(source="main", target=commit_id))
                    self.edge_pairs.add(("main", commit_id))

# Revert commits
    def revert_commit_tree(self,branch):
            if branch == "main":
                self.main_branch()
            else:
                 self.user_branch()
            for i in reversed(self.revert_commits):
                subnode = str(i.get("id")).strip().rstrip(".")
                sub_id = f"sub-{subnode}"
                
                if sub_id not in self.node_ids:
                    self.nodes.append(Node(id=sub_id, label=i.get("message"), size=25))
                    self.node_ids.add(sub_id)
                
                if (subnode, sub_id) not in self.edge_pairs:
                    self.edges.append(Edge(source=subnode, target=sub_id))
                    self.edge_pairs.add((subnode, sub_id))

        


    def render(self):
        config = Config(width=750, height=600, directed=True)
        agraph(nodes=self.nodes, edges=self.edges, config=config)

NMCT=NonMergeCommitTree()
NMCT.normal_commit_tree("main")
NMCT.revert_commit_tree("user")
NMCT.render()

class MergeCommitTree(Main):
    pass
