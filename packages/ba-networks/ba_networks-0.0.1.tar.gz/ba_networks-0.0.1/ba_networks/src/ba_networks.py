class printer:
    def __init__(self):
        self.a = 1

    def time_first_old_node(self):
        print('''
        # degree of node in BA model
        # G = nx.read_gml('/path', label=None), put label = None if label error else no need
        # G = nx.graph(G)
        # nx.draw(G)
        def ba_degree(ti = None, t = None, m = None, beta = None):
            # ti is time since node joined, t is time since starting network, m = initial nodes, beta = 0.5
            k = m * ((t/ti)**beta)
            return k
        
        # time it takes for new node to become the same degree as old node
        def time_to_degree_in_ba(m = None):
            k = ba_degree(m)
            return (m/k) *(t**.5)
        
        # degree distribution
        nx.degree_histogram(G)
        
        nx.average_shortest_path_length(G)
        
        nx.average_clustering(G)
        
        nx.degree_assortativity_coefficient(G) # assortativity
        G = nx.karate_club_graph()
        nx.degree_histogram(G)
        
        
        kn, ksq = 0, 0
        for i, v in enumerate(nx.degree_histogram(G)):
            kn += (i * v)/sum(nx.degree_histogram(G))
            ksq += (i**2 * v)
        print(kn, ksq)     
        ''')

    def network_regime_criticality(self):
        print('''
        import math
        import numpy as np
        from scipy.optimize import fsolve
        
        def expected_links(N, p):
            return p * N * (N - 1) / 2
        
        def critical_probability(N):
            return math.log(N) / N
        
        def network_regime(N, p):
            pc = critical_probability(N)
            if p < pc:
                return "Subcritical"
            elif p > pc:
                return "Supercritical"
            else:
                return "Critical"
        
        def solve_Ncr(p):
            def equation(N):
                return p - math.log(N) / N
            return fsolve(equation, 1000)[0]
        
        def average_degree(N, p):
            return p * (N - 1)
        
        def average_distance(N, k_avg):
            return math.log(N) / math.log(k_avg)
        
        def degree_distribution(k, lambda_val):
            return (math.exp(-lambda_val) * lambda_val**k) / math.factorial(k)
        
        # Given parameters
        N = 3000
        p = 1e-3
        
        # 1. Expected number of links
        L_avg = expected_links(N, p)
        print(f"1. Expected number of links: {L_avg:.2f}")
        print()
        
        # 2. Network regime
        regime = network_regime(N, p)
        print(f"2. Network regime: {regime}")
        print()
        
        # 3. Critical probability
        pc = critical_probability(N)
        print(f"3. Critical probability: {pc:.6f}")
        print()
        
        # 4. Number of nodes for one component
        N_cr = solve_Ncr(p)
        print(f"4. Number of nodes for one component: {N_cr:.2f}")
        print()
        
        # 5. Average degree and distance for the network in (d)
        k_cr_avg = average_degree(N_cr, p)
        d_avg = average_distance(N_cr, k_cr_avg)
        print(f"5. For the network in (d):")
        print(f"   Average degree: {k_cr_avg:.2f}")
        print(f"   Average distance: {d_avg:.2f}")
        print()
        
        # 6. Degree distribution
        lambda_val = average_degree(N, p)
        k_values = range(20)  # Calculate for k = 0 to 19
        pk_values = [degree_distribution(k, lambda_val) for k in k_values]
        
        print("6. Degree distribution:")
        for k, pk in zip(k_values, pk_values):
            print(f"   P({k}) = {pk:.6f}")
        ''')

    def watts_clustering_shortest(self):
        print('''
        import numpy as np
        import networkx as nx
        
        def create_circular_network(N, m):
            G = nx.Graph()
            G.add_nodes_from(range(N))
            for i in range(N):
                for j in range(1, m + 1):
                    G.add_edge(i, (i + j) % N)
                    G.add_edge(i, (i - j) % N)
            return G
        
        def average_clustering_coefficient(N, m):
            # For this specific network structure, we can calculate directly
            if m == 1:
                return 0
            return (3 * (m - 1)) / (2 * (2 * m - 1))
        
        def average_shortest_path(G):
            return nx.average_shortest_path_length(G)
        
        def theoretical_average_shortest_path(N, m):
            return N / (4 * m) + 1/2
        
        # Parameters
        N = 20
        m = 3
        
        # Create the network
        G = create_circular_network(N, m)
        
        # Calculate average clustering coefficient
        C_avg = average_clustering_coefficient(N, m)
        print(f"Average clustering coefficient: {C_avg:.4f}")
        
        # Calculate average shortest path
        d_avg = average_shortest_path(G)
        print(f"Average shortest path: {d_avg:.4f}")
        
        # Theoretical average shortest path
        d_avg_theo = theoretical_average_shortest_path(N, m)
        print(f"Theoretical average shortest path: {d_avg_theo:.4f}")
        
        # Calculate for large N
        N_large = 10000
        C_avg_large = average_clustering_coefficient(N_large, m)
        d_avg_large_theo = theoretical_average_shortest_path(N_large, m)
        
        print(f"For N = {N_large}:")
        print(f"Average clustering coefficient: {C_avg_large:.4f}")
        print(f"Theoretical average shortest path: {d_avg_large_theo:.4f}")
        ''')

    def robustness(self):
        print('''
        # Attack Threshold
        import numpy as np
        import networkx as nx
        import matplotlib.pyplot as plt
        
        # Generate a network with power-law degree distribution (Configuration model)
        def generate_powerlaw_network(N, gamma):
            while True:
                degree_sequence = np.random.zipf(gamma, N)
                # Ensure the sum of degrees is even
                if sum(degree_sequence) % 2 == 0:
                    break
            G = nx.configuration_model(degree_sequence)
            G = nx.Graph(G)  # Remove multi-edges
            G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops
            return G
        
        # Attack the network based on a specific metric and fraction of nodes removed
        def attack_network(G, metric, fraction_remove):
            N = len(G)
            num_nodes_to_remove = int(fraction_remove * N)
        
            if metric == 'degree':
                # Remove nodes with the highest degree
                nodes_sorted_by_metric = sorted(G.degree(), key=lambda x: x[1], reverse=True)
            elif metric == 'clustering':
                # Remove nodes with the highest clustering coefficient
                clustering_coefficients = nx.clustering(G)
                nodes_sorted_by_metric = sorted(clustering_coefficients.items(), key=lambda x: x[1], reverse=True)
        
            nodes_to_remove = [node for node, value in nodes_sorted_by_metric[:num_nodes_to_remove]]
            G.remove_nodes_from(nodes_to_remove)
        
            # Check if there are any connected components left
            if len(G) == 0 or len(list(nx.connected_components(G))) == 0:
                return 0  # No components left
        
            # Get the size of the largest connected component
            largest_cc = max(nx.connected_components(G), key=len)
            return len(largest_cc)
        
        # Visualize the network
        def visualize_network(G, title):
            plt.figure(figsize=(10, 10))
            pos = nx.spring_layout(G, seed=42)  # For better layout and consistent positioning
            nx.draw_networkx_nodes(G, pos, node_size=10, node_color='blue')
            nx.draw_networkx_edges(G, pos, alpha=0.3)
            plt.title(title)
            plt.show()
        
        # Run the attack simulation and visualize the network
        def conspiracy_simulation(N, gamma):
            fractions_removed = np.linspace(0, 1, 20)  # Fractions of nodes to remove
            G = generate_powerlaw_network(N, gamma)
        
            # Visualize the original network
            visualize_network(G, "Original Network")
        
            # Simulate degree-based and clustering coefficient-based attacks
            largest_components_degree = []
            largest_components_clustering = []
        
            for fraction in fractions_removed:
                G_copy1 = G.copy()
                G_copy2 = G.copy()
        
                size_giant_degree = attack_network(G_copy1, 'degree', fraction)
                size_giant_clustering = attack_network(G_copy2, 'clustering', fraction)
        
                largest_components_degree.append(size_giant_degree)
                largest_components_clustering.append(size_giant_clustering)
        
                # Visualize the network after 20% of nodes have been removed
                if fraction == 0.2:  # Visualizing at 20% removal
                    visualize_network(G_copy1, "Network after 20% Degree-based Attack")
                    visualize_network(G_copy2, "Network after 20% Clustering-based Attack")
        
            # Plot the results
            plt.plot(fractions_removed, largest_components_degree, label='Degree-based attack')
            plt.plot(fractions_removed, largest_components_clustering, label='Clustering-based attack')
            plt.xlabel('Fraction of nodes removed')
            plt.ylabel('Size of largest component')
            plt.legend()
            plt.title('Attack on Social Network: Degree vs Clustering Coefficient')
            plt.show()
        
        # Example usage
        N = 500  # Reduced for better visualization
        gamma = 2.5
        conspiracy_simulation(N, gamma)
        ------------------------------------------------------------------
        
        
        Part 2: Simulating Avalanches in Networks
        
        We'll simulate the sandpile model on both an Erdős-Rényi (ER) and a scale-free network.
        ------------------------------------------------------------------
        import random
        import networkx as nx
        import numpy as np
        import matplotlib.pyplot as plt
        
        # Avalanche simulation function with network visualization
        def simulate_avalanches(G, num_steps=10000, grain_loss=1e-4, visualize_step=2000):
            # Initialize bucket sizes (equal to node degrees)
            bucket_sizes = {node: G.degree(node) for node in G.nodes()}
            sand_in_buckets = {node: 0 for node in G.nodes()}
            avalanche_sizes = []
        
            for step in range(num_steps):
                # Add a grain to a random node
                node = random.choice(list(G.nodes()))
                sand_in_buckets[node] += 1
        
                # Perform topplings
                avalanche_size = 0
                unstable_nodes = [node]
        
                while unstable_nodes:
                    current_node = unstable_nodes.pop()
                    if sand_in_buckets[current_node] >= bucket_sizes[current_node]:
                        # Node topples
                        avalanche_size += 1
                        excess_grains = sand_in_buckets[current_node]
                        sand_in_buckets[current_node] = 0  # Reset bucket
        
                        # Distribute grains to neighbors
                        for neighbor in G.neighbors(current_node):
                            sand_in_buckets[neighbor] += (1 - grain_loss)
                            if sand_in_buckets[neighbor] >= bucket_sizes[neighbor]:
                                unstable_nodes.append(neighbor)
        
                avalanche_sizes.append(avalanche_size)
        
                # Visualize the network at the specified step
                if step == visualize_step:
                    visualize_network(G, sand_in_buckets, f"Network at Step {visualize_step} (Avalanche)")
        
            return avalanche_sizes
        
        # Plot avalanche distribution
        def plot_avalanche_distribution(avalanche_sizes, title):
            unique_sizes, counts = np.unique(avalanche_sizes, return_counts=True)
            probabilities = counts / np.sum(counts)
        
            plt.loglog(unique_sizes, probabilities, marker='o', linestyle='none')
            plt.xlabel('Avalanche Size (s)')
            plt.ylabel('P(s)')
            plt.title(title)
            plt.show()
        
        # Generate random network (Erdős-Rényi)
        def generate_erdos_renyi(N, avg_k):
            p = avg_k / (N - 1)
            G = nx.erdos_renyi_graph(N, p)
            return G
        
        # Generate scale-free network
        def generate_scale_free_network(N, gamma):
            # Generate a Zipf degree sequence
            degree_sequence = np.random.zipf(gamma, N)
        
            # Ensure that the sum of the degree sequence is even
            if sum(degree_sequence) % 2 != 0:
                # Adjust by adding 1 to a random node's degree
                degree_sequence[random.randint(0, N - 1)] += 1
        
            # Generate the configuration model graph
            G = nx.configuration_model(degree_sequence)
            G = nx.Graph(G)  # Convert to simple graph
            G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops
            return G
        
        # Visualize the network
        def visualize_network(G, sand_in_buckets=None, title="Network Visualization"):
            plt.figure(figsize=(10, 10))
            pos = nx.spring_layout(G, seed=42)  # For consistent layout
            node_colors = 'blue'
        
            if sand_in_buckets:
                node_colors = [sand_in_buckets[node] for node in G.nodes()]
                nx.draw(G, pos, node_size=50, node_color=node_colors, cmap=plt.cm.Blues, with_labels=False)
            else:
                nx.draw(G, pos, node_size=50, node_color=node_colors, with_labels=False)
        
            plt.title(title)
            plt.show()
        
        # Example usage for both types of networks
        N = 500
        avg_k = 2
        
        # Erdős-Rényi network
        G_er = generate_erdos_renyi(N, avg_k)
        visualize_network(G_er, title="Erdős-Rényi Network (Before Avalanche)")
        avalanche_sizes_er = simulate_avalanches(G_er, visualize_step=2000)
        plot_avalanche_distribution(avalanche_sizes_er, "Avalanche Size Distribution (Erdős-Rényi)")
        
        # Scale-free network (Configuration model)
        G_sf = generate_scale_free_network(N, gamma=2.5)
        visualize_network(G_sf, title="Scale-Free Network (Before Avalanche)")
        avalanche_sizes_sf = simulate_avalanches(G_sf, visualize_step=2000)
        plot_avalanche_distribution(avalanche_sizes_sf, "Avalanche Size Distribution (Scale-Free)")
        -------------------------------------------------------------------------------------------
        BA networks
        ---------------------
        
        import numpy as np
        import networkx as nx
        import matplotlib.pyplot as plt
        import powerlaw
        
        # Parameters
        N = 10_000  # Total number of nodes
        m = 4       # Number of edges to attach from a new node to existing nodes
        intermediate_steps = [100, 1000]
        
        # Generate Barabási-Albert network
        def generate_ba_network(N, m):
            return nx.barabasi_albert_graph(N, m)
        
        # Measure degree distribution
        def degree_distribution(G):
            degrees = np.array(list(dict(G.degree()).values()))
            return np.bincount(degrees), degrees
        
        # Plot degree distribution and fit power-law
        def plot_degree_distribution(degree_counts, label):
            k = np.arange(len(degree_counts))
            plt.loglog(k, degree_counts, marker='o', linestyle='none', label=label)
        
            # Fit to power-law
            fit = powerlaw.Fit(k[degree_counts > 0], discrete=True)
            alpha = fit.alpha
            xmin = fit.xmin
            fit.plot_pdf()
        
            return alpha, xmin
        
        # Plot cumulative degree distribution
        def plot_cumulative_distribution(degree_counts, label):
            k = np.arange(len(degree_counts))
            cumulative_counts = np.cumsum(degree_counts[::-1])[::-1]
            plt.loglog(k, cumulative_counts, marker='o', linestyle='none', label=label)
        
        # Measure average clustering coefficient
        def average_clustering_coefficient(G):
            return nx.average_clustering(G)
        
        # Visualize the network
        def visualize_network(G, title):
            plt.figure(figsize=(8, 8))
            pos = nx.spring_layout(G)  # Use spring layout for a clean display
            nx.draw(G, pos, node_size=10, node_color="blue", edge_color="gray", alpha=0.7)
            plt.title(title)
            plt.show()
        
        # Main analysis
        degree_distributions = {}
        clustering_coefficients = []
        
        # Visualize the network at the start (using the first intermediate step)
        initial_step = intermediate_steps[0]
        initial_G = generate_ba_network(initial_step, m)
        visualize_network(initial_G, f"Barabási-Albert Network (N = {initial_step}, m = {m})")
        
        for t in intermediate_steps:
            G = generate_ba_network(t, m)
            degree_counts, _ = degree_distribution(G)
            degree_distributions[t] = degree_counts
            clustering_coeff = average_clustering_coefficient(G)
            clustering_coefficients.append(clustering_coeff)
        
        # Plot degree distributions
        plt.figure(figsize=(12, 6))
        for t in intermediate_steps:
            plot_degree_distribution(degree_distributions[t], f'N = {t}')
        
        plt.xlabel('Degree (k)')
        plt.ylabel('P(k)')
        plt.title('Degree Distribution of Barabási-Albert Network')
        plt.legend()
        plt.grid()
        plt.show()
        
        # Plot cumulative degree distributions
        plt.figure(figsize=(12, 6))
        for t in intermediate_steps:
            plot_cumulative_distribution(degree_distributions[t], f'N = {t}')
        
        plt.xlabel('Degree (k)')
        plt.ylabel('Cumulative P(k)')
        plt.title('Cumulative Degree Distribution of Barabási-Albert Network')
        plt.legend()
        plt.grid()
        plt.show()
        
        # Plot average clustering coefficient vs N
        plt.figure(figsize=(8, 5))
        plt.plot(intermediate_steps, clustering_coefficients, marker='o')
        plt.xlabel('Number of Nodes (N)')
        plt.ylabel('Average Clustering Coefficient')
        plt.title('Average Clustering Coefficient vs Number of Nodes')
        plt.grid()
        plt.show()
        ------------------------------------------------------------------

        ''')

    def ba_networks(self):
        print('''
        def generate_ba_network(N, m):
            G = nx.complete_graph(m)
            while G.number_of_nodes() < N:
                G = nx.barabasi_albert_graph(G.number_of_nodes() + 1, m, initial_graph=G)
            return G
        
        def measure_degree_distribution(G):
            degrees = [d for n, d in G.degree()]
            return Counter(degrees)
        
        def fit_power_law(x, y):
            logx = np.log(x)
            logy = np.log(y)
            coeffs = np.polyfit(logx, logy, 1)
            return -coeffs[0]
        
        def plot_degree_distribution(distributions, N_values):
            plt.figure(figsize=(10, 6))
            for N, dist in zip(N_values, distributions):
                x = list(dist.keys())
                y = [dist[k] / sum(dist.values()) for k in x]
                plt.loglog(x, y, 'o-', label=f'N = {N}')
        
                # Fit power-law
                gamma = fit_power_law(x, y)
                print(f"N = {N}, γ = {gamma:.2f}")
        
            plt.xlabel('Degree (k)')
            plt.ylabel('P(k)')
            plt.legend()
            plt.title('Degree Distribution at Different Network Sizes')
            plt.show()
        
        def plot_cumulative_distribution(distributions, N_values):
            plt.figure(figsize=(10, 6))
            for N, dist in zip(N_values, distributions):
                x = sorted(dist.keys())
                y = [sum(dist[k] for k in dist if k >= degree) / sum(dist.values()) for degree in x]
                plt.loglog(x, y, '-', label=f'N = {N}')
        
            plt.xlabel('Degree (k)')
            plt.ylabel('P(K ≥ k)')
            plt.legend()
            plt.title('Cumulative Degree Distribution')
            plt.show()
        
        def measure_clustering_coefficient(N_values, m):
            clustering_coeffs = []
            for N in N_values:
                G = generate_ba_network(N, m)
                clustering_coeffs.append(nx.average_clustering(G))
        
            plt.figure(figsize=(10, 6))
            plt.loglog(N_values, clustering_coeffs, 'o-')
            plt.xlabel('N')
            plt.ylabel('Average Clustering Coefficient')
            plt.title('Clustering Coefficient vs. Network Size')
            plt.show()
        
        # Generate BA network and analyze
        N_values = [10**2, 10**3, 10**4]
        m = 4
        
        distributions = []
        for N in N_values:
            G = generate_ba_network(N, m)
            distributions.append(measure_degree_distribution(G))
        
        plot_degree_distribution(distributions, N_values)
        plot_cumulative_distribution(distributions, N_values)
        
        # Measure clustering coefficient
        N_values_clustering = np.logspace(2, 4, 10).astype(int)
        measure_clustering_coefficient(N_values_clustering, m)
        ''')

    def self_multi_loops(self):
        print('''
        import networkx as nx
        import numpy
        
        def generate_network(N, gamma):
            degree_distribution = np.random.zipf(gamma, N)
            if sum(degree_distribution) % 2 != 0:
                degree_distribution[np.argmax(degree_distribution)] -= 1
        
            G = nx.configuration_model(degree_distribution)
            G_simple = nx.Graph(G)
            G_simple.remove_edges_from(nx.selfloop_edges(G_simple))
        
            return G, G_simple
        
        def calculate_percentage(G, G_simple):
            num_edges = G.number_of_edges()
            num_multi_links = num_edges - G_simple.number_of_edges()
        
            num_self_loop = sum(1 for u,v in G.edges() if u == v)
        
            per_multi_links = (num_multi_links/num_edges)*100
            per_self_loop = (num_self_loop/num_edges)*100
        
            return per_multi_links, per_self_loop
        
        def print_results(N_values, gamma_values):
            for gamma in gamma_values:
                print(f"Results for γ = {gamma}:")
        
                for N in N_values:
                    G, G_simple = generate_network(N, gamma)
                    perc_multi_links, perc_self_loops = calculate_percentage(G, G_simple)
        
                    print(f"Network Size (N): {N}")
                    print(f"  Percentage of Multi-links: {perc_multi_links:.2f}%")
                    print(f"  Percentage of Self-loops: {perc_self_loops:.2f}%\n")
        
        N_values = [10**3, 10**4, 10**5]
        gamma_values = [2.2, 3.0]
        print_results(N_values, gamma_values)
        ''')

    def modified_barabasi(self):
        print('''
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.special import gamma
        from collections import Counter
        
        def modified_barabasi_albert(N, m, A):
            # Initialize network with m nodes
            in_degrees = np.zeros(N, dtype=int)
            for i in range(m, N):
                # Calculate attachment probabilities
                if i == m or (A == 0 and in_degrees[:i].sum() == 0):
                    # Uniform distribution for initial nodes or when all in-degrees are zero
                    probabilities = np.ones(i) / i
                else:
                    if A == 0:
                        probabilities = in_degrees[:i] / in_degrees[:i].sum()
                    else:
                        probabilities = (in_degrees[:i] + A) / (in_degrees[:i].sum() + i * A)
        
                # Ensure probabilities are valid
                probabilities = np.nan_to_num(probabilities)
                probabilities /= probabilities.sum()
        
                # Choose m nodes to connect to
                targets = np.random.choice(i, size=m, replace=False, p=probabilities)
        
                # Update in-degrees
                in_degrees[targets] += 1
        
            return in_degrees
        
        def theoretical_distribution(k, m, A):
            return gamma(k + A) * gamma(2 + A/m) / (gamma(A) * gamma(k + 2 + A/m))
        
        # Set parameters
        N = 100000  # Number of nodes
        m = 2       # Number of links for each new node
        A = 1       # Constant A in the attachment probability
        
        # Generate network
        in_degrees = modified_barabasi_albert(N, m, A)
        
        # Calculate degree distribution
        degree_counts = Counter(in_degrees)
        max_degree = max(degree_counts.keys())
        
        # Prepare data for plotting
        x = np.arange(0, max_degree + 1)
        y_empirical = [degree_counts.get(k, 0) / N for k in x]
        y_theoretical = [theoretical_distribution(k, m, A) for k in x]
        
        # Plot results
        plt.figure(figsize=(10, 6))
        plt.loglog(x[1:], y_empirical[1:], 'bo', label='Empirical')
        plt.loglog(x[1:], y_theoretical[1:], 'r-', label='Theoretical')
        plt.xlabel('In-degree (k)')
        plt.ylabel('Probability P(k)')
        plt.legend()
        plt.title(f'In-degree Distribution (N={N}, m={m}, A={A})')
        
        # Calculate and print the power-law exponent
        gamma_theoretical = 2 + A * (1/m - 1)
        print(f"Theoretical power-law exponent: {gamma_theoretical:.2f}")
        
        # Estimate empirical power-law exponent (for k > 10)
        k_fit = x[x > 10]
        y_fit = np.array(y_empirical)[x > 10]
        coeffs = np.polyfit(np.log(k_fit), np.log(y_fit), 1)
        gamma_empirical = -coeffs[0]
        print(f"Estimated empirical power-law exponent: {gamma_empirical:.2f}")
        
        plt.show()
        
        # Out-degree distribution
        print("Out-degree distribution:")
        print(f"All nodes have out-degree {m}")
        
        import networkx as nx
        import matplotlib.pyplot as plt
        
        def generate_and_visualize_network(N, k_avg):
            p = k_avg / (N - 1)
            G = nx.erdos_renyi_graph(N, p)
            plt.figure(figsize=(8, 6))
            nx.draw(G, node_size=20, node_color='lightblue', with_labels=False)
            plt.title(f"N={N}, 〈k〉={k_avg}")
            plt.show()
        
        N = 500
        for k_avg in [0.8, 1, 8]:
            generate_and_visualize_network(N, k_avg)
            
        def calculate_degrees(N, p, q):
            k_blue_avg = p * (N - 1)
            k_full_avg = p * (N - 1) + q * N
            return k_blue_avg, k_full_avg
        
        N = 1000  # Example value
        p = 0.01  # Example value
        q = 0.005  # Example value
        
        k_blue_avg, k_full_avg = calculate_degrees(N, p, q)
        print(f"Average degree of blue subnetwork: {k_blue_avg:.2f}")
        print(f"Average degree of full network: {k_full_avg:.2f}")
        
        import math
        def minimal_probabilities(N):
            p_min = math.log(N) / N
            q_min = math.log(2*N) / (2*N)
            return p_min, q_min
        
        p_min, q_min = minimal_probabilities(N)
        print(f"Minimal p: {p_min:.4f}")
        print(f"Minimal q: {q_min:.4f}")
        
        def fraction_purple_for_interactivity(N, p):
            k_avg = p * (N - 1)
            f_min = 1 / math.sqrt(k_avg)
            return f_min
        
        N = 1000
        p = 0.01
        f_min = fraction_purple_for_interactivity(N, p)
        print(f"Minimum fraction of purple nodes: {f_min:.4f}")
        ''')