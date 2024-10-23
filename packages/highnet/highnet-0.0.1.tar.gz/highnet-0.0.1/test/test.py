from highnet import HighOrderNetwork, page_rank, community_detection

network = HighOrderNetwork(10, 20)

network.add_edge(0, 1)
network.add_edge(1, 2)
network.add_edge(2, 3)
...

pr_values = page_rank(network)

communities = community_detection(network, 3)
