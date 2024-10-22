#include <list>
#include <vector>
#include <stack>


#include "../include/NodeCT.hpp"
#include "../include/ComponentTree.hpp"
#include "../include/AdjacencyRelation.hpp"
#include "../include/AttributeComputedIncrementally.hpp"


int* ComponentTree::countingSort(int* img){
	int n = this->numRows * this->numCols;
	int maxvalue = img[0];
	for (int i = 1; i < n; i++)
		if(maxvalue < img[i]) maxvalue = img[i];
			
	std::vector<int> counter(maxvalue + 1, 0); 
	int *orderedPixels = new int[n];
		
	if(this->isMaxtree()){
		for (int i = 0; i < n; i++)
			counter[img[i]]++;

		for (int i = 1; i < maxvalue; i++) 
			counter[i] += counter[i - 1];
		counter[maxvalue] += counter[maxvalue-1];
		
		for (int i = n - 1; i >= 0; --i)
			orderedPixels[--counter[img[i]]] = i;	

	}else{
		for (int i = 0; i < n; i++)
			counter[maxvalue - img[i]]++;

		for (int i = 1; i < maxvalue; i++) 
			counter[i] += counter[i - 1];
		counter[maxvalue] += counter[maxvalue-1];

		for (int i = n - 1; i >= 0; --i)
			orderedPixels[--counter[maxvalue - img[i]]] = i;
	}
	
	return orderedPixels;
}

int ComponentTree::findRoot(int *zPar, int x) {
	if (zPar[x] == x)
		return x;
	else {
		zPar[x] = findRoot(zPar, zPar[x]);
		return zPar[x];
	}
}

int* ComponentTree::createTreeByUnionFind(int* orderedPixels, int* img) {
	const int n = this->numRows * this->numCols;
	int *zPar = new int[n];
	int *parent = new int[n];
		
	for (int p = 0; p < n; p++) {
		zPar[p] =  -1;
	}
		
	for(int i=n-1; i >= 0; i--){
		int p = orderedPixels[i];
		parent[p] = p;
		zPar[p] = p;
		for (int n : this->adj->getAdjPixels(p)) {
			if(zPar[n] != -1){
				int r = this->findRoot(zPar, n);
				if(p != r){
					parent[r] = p;
					zPar[r] = p;
				}
			}
		}
	}
			
	// canonizacao da arvore
	for (int i = 0; i < n; i++) {
		int p = orderedPixels[i];
		int q = parent[p];
				
		if(img[parent[q]] == img[q]){
			parent[p] = parent[q];
		}
	}
		
	delete[] zPar;
	return parent;		
}

void ComponentTree::reconstruction(NodeCT* node, int* imgOut){
	for (int p : node->getCNPs()){
		imgOut[p] = node->getLevel();
	}
	for(NodeCT* child: node->getChildren()){
		reconstruction(child, imgOut);
	}
}

/*ComponentTree::ComponentTree(int numRows, int numCols, bool isMaxtree){
	this->numRows = numRows;
	this->numCols = numCols;
	this->maxtreeTreeType = isMaxtree;
	this->adj = new AdjacencyRelation(numRows, numCols, 1.5);	
 }*/


void ComponentTree::freeMemory(){
	this->~ComponentTree();
}

 ComponentTree::~ComponentTree(){
	delete this->adj;  
	for (NodeCT *node: this->listNodes){
		delete node;
		node = nullptr;
	}
	delete[] nodes;
	nodes = nullptr;
 }

ComponentTree::ComponentTree(int* img, int numRows, int numCols, bool isMaxtree) 
	: ComponentTree(img, numRows, numCols, isMaxtree, 1.5){ }
 
ComponentTree::ComponentTree(int* img, int numRows, int numCols, bool isMaxtree, double radiusOfAdjacencyRelation){
	this->numRows = numRows;
	this->numCols = numCols;
	this->maxtreeTreeType = isMaxtree;
	this->adj = new AdjacencyRelation(numRows, numCols, radiusOfAdjacencyRelation);	

	int n = this->numRows * this->numCols;
	//this->parent = new int[ n ];
	this->orderedPixels = countingSort(img);
	this->parent = createTreeByUnionFind(orderedPixels, img);
		
	//std::unordered_map<int, NodeCT*> nodes;
	this->nodes = new NodeCT*[n];


	this->numNodes = 0;
	for (int i = 0; i < n; i++) {
		int p = orderedPixels[i];
		if (p == parent[p]) { //representante do node raiz
			this->root = this->nodes[p] = new NodeCT(this->numNodes++, p, nullptr, img[p]);
			this->listNodes.push_back(this->nodes[p]);
			this->nodes[p]->addCNPs(p);
		}
		else if (img[p] != img[parent[p]]) { //representante de um node
			this->nodes[p] = new NodeCT(this->numNodes++, p, this->nodes[parent[p]], img[p]);
			this->listNodes.push_back(this->nodes[p]);
			this->nodes[p]->addCNPs(p);
			this->nodes[parent[p]]->addChild(this->nodes[p]);
		}
		else if (img[p] == img[parent[p]]) {
			this->nodes[parent[p]]->addCNPs(p);
			this->nodes[p] = this->nodes[parent[p]];
		}
	}
	
	AttributeComputedIncrementally::computerAttribute(this->root,
		[](NodeCT* _node) -> void { //pre-processing
			_node->setAreaCC( _node->getCNPs().size() );
			_node->setNumDescendants( _node->getChildren().size() );
		},
		[](NodeCT* _root, NodeCT* _child) -> void { //merge-processing
			_root->setAreaCC( _root->getAreaCC() + _child->getAreaCC() );
			_root->setNumDescendants( _root->getNumDescendants() + _child->getNumDescendants() );
		},
		[](NodeCT* node) -> void { //post-processing
									
		}
	);
}


int* ComponentTree::getOrderedPixels(){
	return this->orderedPixels;
}

int* ComponentTree::getParent(){
	return this->parent;
}

NodeCT* ComponentTree::getSC(int pixel){
	return this->nodes[pixel];
}
	
NodeCT* ComponentTree::getRoot() {
	return this->root;
}

bool ComponentTree::isMaxtree(){
	return this->maxtreeTreeType;
}

std::list<NodeCT*> ComponentTree::getListNodes(){
	return this->listNodes;
}

int ComponentTree::getNumNodes(){
	return this->numNodes;
}

int ComponentTree::getNumRowsOfImage(){
	return this->numRows;
}

int ComponentTree::getNumColsOfImage(){
	return this->numCols;
}

int* ComponentTree::getImageAferPruning(NodeCT* nodePruning){
	int n = this->numRows * this->numCols;
	int* imgOut = new int[n];
	std::stack<NodeCT*> s;
	s.push(this->root);
	while(!s.empty()){
		NodeCT* node = s.top();s.pop();
		if(node->getIndex() == nodePruning->getIndex()){
			for(int p: node->getPixelsOfCC()){
				if(node->getParent() != nullptr)
					imgOut[p] = node->getParent()->getLevel();
				else
					imgOut[p] = node->getLevel();
			}
		}
		else{
			for(int p: node->getCNPs()){
				imgOut[p] = node->getLevel();
			}
			for(NodeCT* child: node->getChildren()){
				s.push(child);
			}
		}
	}
	return imgOut;
}

void ComponentTree::pruning(NodeCT* nodePruning){
	if(nodePruning->getParent() != nullptr){
		for(int p: nodePruning->getPixelsOfCC()){
			nodePruning->getParent()->addCNPs(p);
			this->nodes[p] = nodePruning->getParent()->getParent();
		}
		int numDescendants = nodePruning->getParent()->getNumDescendants();
		int numDescendantsChild = nodePruning->getNumDescendants() + 1;
		nodePruning->getParent()->setNumDescendants(numDescendants - numDescendantsChild); 
		nodePruning->getParent()->getChildren().remove(nodePruning);
		nodePruning->setParent(nullptr);
		nodePruning = nullptr;
		free(nodePruning);

	}
}

int* ComponentTree::reconstructionImage(){
	int n = this->numRows * this->numCols;
	int *imgOut = new int[n];
	this->reconstruction(this->root, imgOut);
	return imgOut;
}

int* ComponentTree::getInputImage(){
	int n = this->numRows * this->numCols;
	int* img = new int[n];
	this->reconstruction(this->root, img);
	return img;
}
	