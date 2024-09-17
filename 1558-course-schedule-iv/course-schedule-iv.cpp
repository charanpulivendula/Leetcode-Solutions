class Solution {
public:
    unordered_map<int,int> vis;
    vector<vector<int>> adj;
    unordered_map<int,unordered_map<int,int>> m;
    int n;
    void dfs(int s,int x)
    {
        vis[s]++;
        for(auto& y:adj[s])
        {
            if(vis.find(y)==vis.end())
            {
                m[x][y]++;
                dfs(y,x);
            }
        }
    }
    vector<bool> checkIfPrerequisite(int n, vector<vector<int>>& a, vector<vector<int>>& q) {
        
        this->n=n;
        this->adj.resize(n);
        vector<bool> ans;

        // reversing the edges to traverse to ancestors

        for(int i=0;i<a.size();i++)
        {
            adj[a[i][1]].push_back(a[i][0]);
        }

        for(int i=0;i<n;i++)
        {
            dfs(i,i);
            vis.clear();
        }

        for(int j=0;j<q.size();j++)
        {
            if(m[q[j][1]].find(q[j][0])!=m[q[j][1]].end())
             ans.push_back(true);
            else
             ans.push_back(false);
        }

        return ans;


         
    }
};