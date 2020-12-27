#include <iostream>
#include <vector>

int main(){
	int max_num=100;
	std::vector<int> v1;
	v1.reserve(max_num);
	int i = 0;
	while(i<max_num){
		v1.push_back(i);
		i++;
	}
	for (auto v:v1){
		std::cout<<v<<std::endl;
	}
	return 0;
}
