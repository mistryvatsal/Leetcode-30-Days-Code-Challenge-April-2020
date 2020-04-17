/*
 * Created on Fri Apr 17 2020
 *
 * Title:
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void breadth_first_search(vector<vector<char>>& grid, int i, int j) {
        if(i<0 || i>=grid.size() || j<0 || j>=grid[i].size() || grid[i][j]=='0') {
            return;
        }

        grid[i][j] = '0';

        breadth_first_search(grid, i+1, j);
        breadth_first_search(grid, i-1, j);
        breadth_first_search(grid, i, j+1);
        breadth_first_search(grid, i, j-1);
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for(int i=0; i<grid.size(); ++i) {
            for(int j=0; j<grid[i].size(); ++j) {
                if(grid[i][j] == '1') {
                    count += 1;
                    breadth_first_search(grid, i, j);
                }
            }
        }   
        return count;     
    }
};