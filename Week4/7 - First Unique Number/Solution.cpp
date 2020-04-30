/*
 * Created on Thu Apr 30 2020
 *
 * Title: Leetcode - First Unique Number
 *
 * Author: Vatsal Mistry
 * Web: mistryvatsal.github.io
 */

#include <iostream>
#include <unordered_map>
#include <list>
#include <vector>

using namespace std;

class FirstUnique {
public:
    unordered_map<int, list<int>::iterator> map;
    list<int> nums_list;

    FirstUnique(vector<int>& nums) {
        for(auto n : nums) {
           add(n);
        }
    }
    
    int showFirstUnique() {
        if(!nums_list.empty()) {
            return nums_list.front();
        }
        return -1;
    }
    
    void add(int value) {
        if(map.find(value) != map.end()) {
            list<int>::iterator it = map[value];
            if(it != nums_list.end()) {
                nums_list.erase(it);
                map[value] = nums_list.end();
            }
        }
        else {
            nums_list.push_back(value);
            list<int>::iterator it = nums_list.end();
            it--;
            map[value] = it;
        }
    }
};