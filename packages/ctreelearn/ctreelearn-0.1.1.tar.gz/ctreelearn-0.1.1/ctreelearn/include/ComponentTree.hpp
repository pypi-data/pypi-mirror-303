#include <list>
#include <vector>

#include "../include/NodeCT.hpp"
#include "../include/AdjacencyRelation.hpp"

#ifndef COMPONENT_TREE_H
#define COMPONENT_TREE_H


class ComponentTree {

protected:
    //int* img;
	int numCols;
	int numRows;
	bool maxtreeTreeType;
	NodeCT* root;
	AdjacencyRelation* adj;
	int* parent;
	int *orderedPixels;
	int numNodes;
	std::list<NodeCT*> listNodes;
	NodeCT** nodes;

	int* countingSort(int* img);
	int* createTreeByUnionFind(int* orderedPixels, int* img);
	int findRoot(int *zPar, int x);
	void reconstruction(NodeCT* node, int* imgOut);

public:
   	
	//ComponentTree(int numRows, int numCols, bool isMaxtree);

	ComponentTree(int* img, int numRows, int numCols, bool isMaxtree, double radiusOfAdjacencyRelation);

	ComponentTree(int* img, int numRows, int numCols, bool isMaxtree);

    ~ComponentTree();

	void freeMemory();

	int* getInputImage();
	
	NodeCT* getRoot();

	bool isMaxtree();

	NodeCT* getSC(int pixel);

	std::list<NodeCT*> getListNodes();

	int getNumNodes();

	int getNumRowsOfImage();

	int getNumColsOfImage();

	int* reconstructionImage();

	int* getParent();

	int* getOrderedPixels();

	int* getImageAferPruning(NodeCT* node);

	void pruning(NodeCT* node);
	
};

#endif