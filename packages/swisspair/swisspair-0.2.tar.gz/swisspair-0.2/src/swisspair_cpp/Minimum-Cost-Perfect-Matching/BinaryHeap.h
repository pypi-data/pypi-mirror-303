#pragma once

#include "Globals.h"
#include "types.h"
#include <vector>
using namespace std;

/*
This is a binary heap for pairs of the type (T_WEIGHT key, int satellite)
It is assumed that satellites are unique integers
This is the case with graph algorithms, in which satellites are vertex or edge indices
 */
class BinaryHeap
{
public:
	BinaryHeap(): satellite(1), size(0) {};

	//Inserts (key k, satellite s) in the heap
	void Insert(T_WEIGHT k, int s);
	//Deletes the element with minimum key and returns its satellite information
	int DeleteMin();
	//Changes the key of the element with satellite s
	void ChangeKey(T_WEIGHT k, int s);
	//Removes the element with satellite s
	void Remove(int s);
	//Returns the number of elements in the heap
	int Size();
	//Resets the structure
	void Clear();

private:
	vector<T_WEIGHT> key;//Given the satellite, this is its key
	vector<int> pos;//Given the satellite, this is its position in the heap
	vector<int> satellite;//This is the heap!

	//Number of elements in the heap
	int size;
};



