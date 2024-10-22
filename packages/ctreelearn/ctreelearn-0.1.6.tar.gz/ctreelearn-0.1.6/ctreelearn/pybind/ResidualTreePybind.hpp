#include <list>

#include "../include/NodeCT.hpp"
#include "../include/NodeRes.hpp"
#include "../include/AttributeOpeningPrimitivesFamily.hpp"
#include "../include/ResidualTree.hpp"

#include "../pybind/PybindUtils.hpp"

#ifndef RESIDUAL_TREE_PYBIND_H
#define RESIDUAL_TREE_PYBIND_H


class ResidualTreePybind: public ResidualTree{

    public:
    using ResidualTree::ResidualTree;

        ResidualTreePybind(AttributeOpeningPrimitivesFamily* primitivesFamily): ResidualTree(primitivesFamily){}

        py::array_t<int> reconstruction(){
            int* imgOutput = ResidualTree::reconstruction();
            return PybindUtils::toNumpy(imgOutput, this->tree->getNumRowsOfImage() * this->tree->getNumColsOfImage());
        }

        py::array_t<int> filtering(py::array_t<float> &attr, float threshold){
            auto bufAttribute = attr.request();
            float *attribute = (float *) bufAttribute.ptr;
            int n = this->tree->getNumRowsOfImage() * this->tree->getNumColsOfImage();
            int* imgOutput = new int[n];

            ResidualTree::filtering(attribute, threshold, imgOutput);
            return PybindUtils::toNumpy(imgOutput, n);
        }

        py::array_t<int> getMaxConstrastImage(){
        return PybindUtils::toNumpy(ResidualTree::getMaxConstrastImage(), this->tree->getNumColsOfImage() * this->tree->getNumRowsOfImage());
        }       

        py::array_t<int> getAssociatedImage(){
        return PybindUtils::toNumpy(ResidualTree::getAssociatedImage(), this->tree->getNumColsOfImage() * this->tree->getNumRowsOfImage());
        }

        py::array_t<int> getAssociatedColoredImage(){
        return PybindUtils::toNumpy(ResidualTree::getAssociatedColorImage(), this->tree->getNumColsOfImage() * this->tree->getNumRowsOfImage() * 3);
        }

};

#endif