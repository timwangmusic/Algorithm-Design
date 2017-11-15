// This class implements Bellman-Ford Algorithm
// For directed/undirected graphs without negative cycles
import java.util.Arrays;

public class Bellman_ford{
	double[] distances;
	int[] vertexes;
	double[][] edges;			// weights for each pair of nodes, infinity means they are not connected
	int networkSize;
	
	public Bellman_ford(int[] vertexes, double[][] edges)
	{
		this.vertexes = vertexes;
		this.networkSize = vertexes.length;
		this.distances = new double[vertexes.length];
		this.edges = edges;
	}
	

	public void shortestPath(int t)
	{
		// Find shortest distance to the target from all other nodes
		Arrays.fill(this.distances, Double.POSITIVE_INFINITY);
		this.distances[t] = 0;
		
		int V = this.networkSize;
		int count = 1;
		while (count < V)
		{
			count++;
			double[] temp = new double[V];
			Arrays.fill(temp, Double.POSITIVE_INFINITY);
			temp[t] = 0;
			
			for (int n = 0; n < V; n++)
			{
				if (n != t)
				{
					double[] dist_to_m = this.edges[n];
					for (int m = 0; m < V; m++)
					{
						temp[n] = Math.min(this.distances[m] + dist_to_m[m], temp[n]);
					}
				}
			}
			this.distances = temp;
		}		
		
	}
	
	public static void main(String[] args) {
		double[][] edges = {
				{0, 5, 2, -1},
				{-2, 0, -2, -2},
				{-1, 3, 0, Double.POSITIVE_INFINITY}, 
				{2, 4, Double.POSITIVE_INFINITY, 0}};
		int[] vertexes = {1,2,3,4};
		Bellman_ford bf = new Bellman_ford(vertexes, edges);
		bf.shortestPath(2);
		for (double dist: bf.distances)
		{
			System.out.println(dist);
		}
		// Output: 1.0, -2.0, 0.0, 2.0
	}
	
}
