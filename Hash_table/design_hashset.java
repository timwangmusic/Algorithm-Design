class MyHashSet {
    TreeSet t = new TreeSet();
    
    public MyHashSet() {
    }
    
    public void add(int key) {
        if (!t.contains(key)){
            t.add(key);
        }
    }
    
    public void remove(int key) {
        if (t.contains(key)){
            t.remove(key);
        }
    }
    
    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return t.contains(key);
    }
}
