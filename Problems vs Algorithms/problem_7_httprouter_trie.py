# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root

        for dir in paths:
            if dir not in current.children:
                current.insert(dir)
            current = current.children[dir]

        current.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root

        for dir in paths:
            if dir not in current.children:
                return None
            current = current.children[dir]

        return current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler = None, not_found_404 = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_404 = not_found_404

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "/":
            return self.route_trie.root.handler
        paths = self.split_path(path)
        result_handler = self.route_trie.find(paths)
        if result_handler is not None:
            return result_handler
        return self.not_found_404


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        paths = path.split("/")
        if paths[-1] == "":
            del paths[-1]
        return paths

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the '' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/contact", "contact handler")
router.add_handler("/home/shop/clothing/randomitem", "item handler")

# # some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'
print(router.lookup("/home/contact/me"))  # should print 'not found handler'
print(router.lookup("/home/shop/clothing/randomitem"))# should print 'item handler'
print(router.lookup("/home/clothing/randomitem/home"))# should print 'not found handler'
print(router.lookup("")) # should print 'root handler'
