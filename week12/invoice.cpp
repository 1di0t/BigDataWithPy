/**************************************************************
 * Invoice 클래스의 구현 파일                                 *
 **************************************************************/
#include "invoice.h"

Invoice::Invoice(int invoiceTelNum,string n,string t):invoiceNumber(invoiceNumber),myCompany(n,t)//dependency
{}

// 생성자
//Invoice::Invoice(int invNum,Company company)
//: invoiceNumber(invNum), invoiceTotal(0.0),myCompany(company)
//{  
//}
// 소멸자
Invoice::~Invoice() 
{
}
void Invoice::add(int quantity, Product product)
{
	invoiceTotal += quantity * product.getPrice();

}
// add 멤버 함수
//void Invoice::add(int quantity, Product product)//use product
//{
//  invoiceTotal += quantity * product.getPrice();
//}
// print 멤버 함수
void Invoice::print() const
{
   cout << "청구 번호: " << invoiceNumber << endl;
   cout << "청구 금액: " << invoiceTotal << endl;
   
   //cout << "회사명: " << myCompany.getName() << endl;
}