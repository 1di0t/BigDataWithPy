/**************************************************************
 * Invoice 클래스의 인터페이스 파일                           *
 **************************************************************/
#ifndef INVOICE_H
#define INVOICE_H
#include "product.h"
#include "company.h"

class Invoice// : 이 없음 => 상속이 아님
{
  private://product의 필드를 가지고 있지 않음
    int invoiceNumber;
    double invoiceTotal; 
    //has : aggregation
    Company myCompany;
  public: 
     Invoice(int invoiceTelNum,string companyName,string companyTel);
    //Invoice(int invoiceNumber,Company myCompany);//has
    ~Invoice(); 
    void add(int quantity, Product product);//use : INVOICE에서 일반 함수에서 product를 가져다 씀(dependency) 
    void print() const; 
};
#endif