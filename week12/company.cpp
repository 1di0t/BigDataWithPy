#include "company.h"

Company::Company(string company, string telNum):myCompany(company),telNum(telNum)
{
}

Company::~Company()
{
}

string Company::getName() const
{
	return myCompany;
}

string Company::getTel() const
{
	return telNum;
}
