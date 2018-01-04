// Copyright 2017 Shuang Zhao zs1995@bu.edu
// Copyright 2017 XintongHao hxtong@bu.edu
// Copyright 2017 LijunXiao ljxiao@bu.edu

#include <stdlib.h>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#define ALPHABETS 26

typedef std::vector <std::vector <char>> wordlist;

struct offset {
 public:
  int d = 0;
  wordlist wordlist_0;
  void wordlist_1(int dd);
  void display(int n);
};

struct node {
 public:
  char path;
  struct node *path_0;
  struct node *letter[ALPHABETS];
  std::string w = "";
  bool F = false;
};

void offset::wordlist_1(int dd) {
  d = dd;
  wordlist_0.clear();
  wordlist_0.resize(d, std::vector <char> (dd, 0));
}

int method(std::vector <std::string> tree, offset *point,
           node *wordtrie,
           std::vector <int> len,
           std::map <int, char> Map,
           std::vector <std::string> *words,
           std::set <std::string> *Map_set);
node * head;

int build_trie(std::vector <std::string> tree, offset *point,
               std::vector <int> len,
               node *wordtrie,
               std::map <int, char> *Map,
               int unit0, int unit1,
               std::vector <std::string> *words,
               std::set <std::string> *Map_set
              ) {
  if (!wordtrie) return false;
  std::map <int, char> Map_trie;
  Map_trie.insert(Map->begin(), Map->end());
  (Map_trie)[unit0 + unit1 * point->d] = wordtrie->path;
  for (const auto &pointer : (*Map))
    if (wordtrie->F) {
      std::vector <int> trie_len = len;
      trie_len.erase(trie_len.begin());
      std::vector <std::string> words_trie = *words;
      words_trie.push_back(wordtrie->w);
      for (const auto &pointer : (words_trie))
        if (method(tree, point, head, trie_len,
                   Map_trie, &words_trie, Map_set)) {
          *words = words_trie;
          *Map = Map_trie;
          return true;
        } else {
          return false;
        }
    }
  int Min_0 = (unit0 - 1 > 0) ? unit0 - 1 : 0;
  int Min_1 = (unit1 - 1 > 0) ? unit1 - 1 : 0;
  int Max_0 = (unit0 + 1 < point->d) ? unit0 + 1 : point->d - 1;
  int Max_1 = (unit1 + 1 < point->d) ? unit1 + 1 : point->d - 1;
  for (int i = Min_0; i <= Max_0; i++) {
    for (int j = Min_1; j <= Max_1; j++) {
      if (Map_trie.count(i + j * point->d))
        continue;
      char target;
      try {
        target = point->wordlist_0.at(i).at(j);
      } catch(std::out_of_range) {
        continue;
      }
      if (wordtrie->letter[target - 'a']) {
        if (build_trie(tree, point, len,
                       wordtrie->letter[point->wordlist_0.at(i).at(j) - 'a'], &
                       Map_trie, i, j, words, Map_set)) {
          Map->insert(Map_trie.begin(), Map_trie.end());
          return true;
        }
      }
    }
  }
  return false;
}

bool initial(const int& tree_len,
             const std::vector<std::vector <char>>& result,
             const std::vector <std::string>& tree,
             std::vector <int> *len, offset *point) {
  point->wordlist_1(tree_len);
  for (int i = 0; i < point->d; i++) {
    for (int j = 0; j < result.size(); j++) {
      point->wordlist_0[i][j] = result[result.size() - 1 - j][i];
    }
  }
  for (auto &k : tree) {
    len->push_back(k.length());
  }
  if (len->size() == 0 || point->d == 0)
    return false;
  return true;
}

int method(std::vector <std::string> tree, offset *point,
           node *wordtrie,
           std::vector <int> len,
           std::map <int, char> Map,
           std::vector <std::string> *words,
           std::set <std::string> *Map_set) {
  if (len.size() == 0) {
    std::string ww = "";
    for (const auto &pointer : *words)
      ww += pointer + " ";
    Map_set->insert(ww);
    return false;
  }
  offset unit_trie = *point;
  for (std::map <int, char>::reverse_iterator Map_new = Map.rbegin();
       Map_new != Map.rend(); ++Map_new) {
    unit_trie.wordlist_0[Map_new->first % unit_trie.d].erase(
      unit_trie.wordlist_0[Map_new->first % unit_trie.d].begin()
      + Map_new->first / unit_trie.d);
  }
  for (int i = 0; i < unit_trie.wordlist_0.size(); i++) {
    for (int j = 0; j < unit_trie.wordlist_0.at(i).size(); j++) {
      std::map <int, char> Map_trie;
      std::vector <std::string> words_trie = *words;
      std::string s0, s1;
      if (words_trie.size() != 0) {
        for (int ii = 0; ii < words_trie.size(); ii++) {
          s0 = words_trie[ii];
          s1 = tree[ii];
          int count = 0;
          for (int jj = 0; jj < s0.size(); jj++) {
            if (s1[jj] != '*') {
              if (s0[jj] == s1[jj])
                count++;
            } else {
              count++;
            }
          }
          if (count != s0.size()) {
            return false;
          }
        }
      }
      if (wordtrie->letter[len.front()]) {
        if (build_trie(tree, &unit_trie, len,
                       wordtrie->letter[len.front()]->letter[unit_trie.
                           wordlist_0.at(i).at(j) - 'a'],
                       &Map_trie, i, j, &words_trie, Map_set)) {
          *words = words_trie;
          return true;
        }
      }
    }
  }
  return false;
}

int whole_list(std::string ss, node *wordtrie) {
  std::ifstream infile(ss);
  std::string word_file;
  int count;
  while (infile >> word_file) {
    if (word_file.length() > ALPHABETS)
      continue;
    count++;
    if (wordtrie->letter[word_file.length()] == NULL) {
      wordtrie->letter[word_file.length()] = new node;
      wordtrie->letter[word_file.length()]->path_0 = wordtrie;
      wordtrie->letter[word_file.length()]->path = '0' + word_file.length();
    }
    node * traverse = wordtrie->letter[word_file.length()];
    for (auto target : word_file) {
      if (traverse->letter[target - 'a'] == NULL) {
        traverse->letter[target - 'a'] = new node;
        traverse->letter[target - 'a']->path_0 = traverse;
        traverse->letter[target - 'a']->path = target;
      }
      traverse = traverse->letter[target - 'a'];
    }
    traverse->F = true;
    traverse->w = word_file;
  }
  return count;
}

std::vector <std::string> word_split(const std::string& word_file,
                                     const std::string& target) {
  std::vector <std::string> word_s;
  std::string::size_type aa, bb;
  bb = word_file.find(target);
  aa = 0;
  while (std::string::npos != bb) {
    word_s.push_back(word_file.substr(aa, bb - aa));
    aa = bb + target.size();
    bb = word_file.find(target, aa);
  }
  if (aa != word_file.length())
    word_s.push_back(word_file.substr(aa));
  return word_s;
}

int main(int argc, char **argv) {
  node wordtrie = node();
  node wordtrie_len = node();
  whole_list(argv[1], &wordtrie);
  whole_list(argv[2], &wordtrie_len);
  while (true) {
    int flag = 0;
    offset point = offset();
    std::string str;
    wordlist result;
    std::string units;
    std::string line = "";
    while (std::cin) {
      if (std::cin.eof()) exit(0);
      getline(std::cin, line);
      if (line == "") exit(0);
      if (line.find("*") == std::string::npos) {
        std::vector<char> data(line.begin(), line.end());
        result.push_back(data);
      } else {
        units = line;
        break;
      }
    }
    int tree_len = result[0].size();
    std::vector <std::string> tree = word_split(units, " ");
    head = &wordtrie;
    std::map <int, char> Map;
    std::vector <int> len;
    if (!initial(tree_len, result, tree, &len, &point))
      return false;
    std::vector<std::string> words;
    std::set<std::string> Map_set;
    method(tree, &point, &wordtrie, len, Map, &words, &Map_set);
    if (Map_set.size() == 0) {
      head = &wordtrie_len;
      method(tree,
             &point, &wordtrie_len, len, Map, &words, &Map_set);
    }
    for (const auto &pointer : Map_set)
      std::cout << pointer << std::endl;
    std::cout << "." << std::endl;
  }
}
