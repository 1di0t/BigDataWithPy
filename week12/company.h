#pragma once
#ifndef COMPANY_H
#define COMPANY_H
#include <string>

using namespace std;

class Company
{
private:
    string myCompany;
    string telNum;
public:
    Company(string name, string telNum);
    ~Company();
    string getName() const;
    string getTel() const;
};
#endif
