
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict={}
        for key,value in edges:
            if key in self.graph_dict:
                self.graph_dict[key].append(value)
            else:
                self.graph_dict[key]=[value]
        print("directed graph formed :",self.graph_dict)
    
    def all_paths(self,start,end,path=[]):
        path=path+[start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.all_paths(node,end,path)
                print("new paths :",new_paths)
            paths.extend(new_paths)
        return paths




if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    print("Inside main")
    graph_obj = Graph(routes)
    start="Mumbai"
    end="New York"
    print(f"all paths from {start} to {end} are :",graph_obj.all_paths(start,end))

