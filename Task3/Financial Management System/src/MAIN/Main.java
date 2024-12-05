package MAIN;

import MODEL.*;
import VIEW.*;
import CONTROLLER.*;

public class Main {

    public static void main(String[] args) {
        

        Customer customer = new Customer("C001", "Alice Smith", "123 Elm Street", "555-1234");

        CustomerView customerView = new CustomerView();
        
        CustomerController customerController = new CustomerController(customer, customerView);
        
        customerController.showCustomerDetails();
        
        customerController.updateCustomerAddress("456 Oak Avenue");
        customerController.showCustomerDetails();
    
        customerController.updateCustomerPhoneNumber("555-5678");
        customerController.showCustomerDetails();
        
        Employee employee = new Employee("E001", "John Doe", "Software Engineer", 80000.0);
        
        EmployeeView employeeView = new EmployeeView();
        EmployeeController employeeController = new EmployeeController(employee, employeeView);
        
        employeeController.showEmployeeDetails();
        
        employeeController.updateEmployeePosition("Senior Software Engineer");
        employeeController.showEmployeeDetails();
    
        Loan loan = new Loan(10000.0, 0.05, 5); 
        
        // Create a LoanView object
        LoanView loanView = new LoanView();
        
        // Create a LoanController object
        LoanController loanController = new LoanController(loan, loanView);
        
        Offer offer = new Offer(1000.0, 0.10, 30); 
        
        // Create an OfferView object
        OfferView offerView = new OfferView();
        
    
        OfferController offerController = new OfferController(offer, offerView);
        
        
        offerController.showOfferDetails();
        
       
        offerController.applyDiscount();
        
       
        offerController.updateDiscountRate(0.15); 
        offerController.applyDiscount();
        
        
        offerController.updateOfferDuration(45);
    }
}
