public class Bellman_ford{
	double[] distances;
	int[] vertexes;
	double[][] edges;			// weights for each pair of nodes, infinity means they are not connected
	
	public Bellman_ford(int[] vertexes, double[][] edges)
	{
		this.vertexes = vertexes;
		this.distances = new double[vertexes.length];
		this.edges = edges;
	}
	

	public void shortestPath(int t)
	{
		// Find shortest distance to the target from all other nodes
		for (int i = 0; i < this.vertexes.length; i++) this.distances[i] = Double.POSITIVE_INFINITY;
		this.distances[t] = 0;
		
		int V = this.vertexes.length;
		int count = V;
		while (count > 0)
		{
			count--;
			double[] temp = new double[V];
			for (int n = 0; n < V && n != t; n++)
			{
				double[] dist_to_m = this.edges[n];
				for (int m = 0; m < V && m != t; m++)
				{
					temp[n] = Math.min(this.distances[m] + dist_to_m[m], this.distances[n]);
				}
			}
			this.distances = temp;
		}		
		
	}
	
	public static void main(String[] args) {
		double[][] edges = {{0.0,1.2,3.5},{1.2,0.0,6.0},{3.5,6.0,0.0}};
		int[] vertexes = {1,2,3};
		Bellman_ford bf = new Bellman_ford(vertexes, edges);
		bf.shortestPath(1);
		for (double dist: bf.distances)
		{
			System.out.println(dist);
		}
	}
	
}

