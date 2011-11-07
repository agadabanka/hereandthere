/*
 *  SRM203Div2.cpp
 *  topcoder_xcode
 *
 *  Created by Amith Raghavendra on 11/5/11.
 *  
 */

#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef vector< vector<string> > vecstrvec;
typedef vector<string> vecstr;

class CalcButton
{
public:
	string getDigits(vecstr sequence){
		string s("");
		map<string, int> digits;
		string maxdigits("");
		int maxfreq = 0;
		
		for(vecstr::iterator it=sequence.begin(); it!=sequence.end(); ++it){
			s += *it;
		}

		for (int i=0; i<s.length()-2; ++i) 	//Till last but 3					
			digits[s.substr(i, 3)]++;		
		
		for (map<string,int>::iterator it=digits.begin(); it!=digits.end(); ++it){
			if (it->second > maxfreq){
				maxfreq = it->second;
				maxdigits = it->first;
			}
		}
		
		return maxdigits;
	}
	
};



int main()
{
    const char *i1[] = { "10000200" };
    const char *i2[] = {"777777777"};
    const char *i3[] = { "6503", "210"};
    const char *i4[] = { "0993034", "6", "4137", "45959935", "25939", "93993", "0", "9358333"};
	
    vector<string> input_1(i1, i1+1);
    vector<string> input_2(i2, i2+1);
    vector<string> input_3(i3, i3+2);
    vector<string> input_4(i4, i4+8);
	
    vecstrvec vecvec;
    vecvec.push_back(input_1);
    vecvec.push_back(input_2);
    vecvec.push_back(input_3);
    vecvec.push_back(input_4);
	
    CalcButton *cb = new CalcButton();
	
    for(vecstrvec::iterator it = vecvec.begin(); it != vecvec.end(); ++it){
        cout << cb->getDigits(*it) << endl;
    }
	
}
