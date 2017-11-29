/**
 * Leetcode 56
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        // after sorting by start time, 
        // the interval start later can only overlap with the last processed/merged interval.
        Collections.sort(intervals, new Comparator<Interval>(){
            public int compare(Interval a, Interval b){
                return a.start - b.start;
            }
        });
        
        List<Interval> res = new ArrayList<>();
        
        for (Interval x: intervals){
            if (res.size() == 0 || res.get(res.size()-1).end < x.start){
                res.add(x);
            }
            else{
                Interval last = res.remove(res.size()-1);
                Interval temp = new Interval(last.start, Math.max(last.end, x.end));
                res.add(temp);
            }
        }      
        return res;
    }
}
