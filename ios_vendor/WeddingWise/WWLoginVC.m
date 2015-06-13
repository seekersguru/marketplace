//
//  WWLoginVC.m
//  WeddingWise
//
//  Created by Deepak Sharma on 5/20/15.
//  Copyright (c) 2015 DS. All rights reserved.
//

#import "WWLoginVC.h"
#import "WWRegistrationVC.h"
#import "UITextField+ADTextField.h"
#import "WWCommon.h"
#import "ViewController.h"
#import "WWCalendarView.h"
#import "WWForgotPassword.h"
#import "AppDelegate.h"

@interface WWLoginVC ()

@end
//Client secret= r4c6Lvxfq99AGauizFsS-Ffw
//Bundle id: com.weddingwise.app



@implementation WWLoginVC


#pragma mark View life cycle methods:
- (void)viewDidLoad {
    [self setTextFieldPlacehoder];
    
    UITapGestureRecognizer *tap = [[UITapGestureRecognizer alloc]
                                   initWithTarget:self
                                   action:@selector(dismissKeyboard)];
    [self.view addGestureRecognizer:tap];
    
    [self.navigationController.navigationBar setHidden:YES];
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
}

-(IBAction)btnBackPressed:(id)sender{
    [self dismissKeyboard];
    [self.navigationController popViewControllerAnimated:YES];
}

#pragma mark IBAction & utility methods:
-(void)dismissKeyboard {
    [_txtEmailAddress resignFirstResponder];
    [_txtPassword resignFirstResponder];
}
-(void)setTextFieldPlacehoder{
    [_txtEmailAddress setTextFieldPlaceholder:@"Email Address" withcolor:[UIColor darkGrayColor] withPadding:_txtEmailAddress];
    [_txtPassword setTextFieldPlaceholder:@"Password" withcolor:[UIColor darkGrayColor] withPadding:_txtPassword];
}
-(IBAction)btnSignInPressed:(id)sender{
    if([self checkValidations]){
        //Call web service
        
        [[AppDelegate sharedAppDelegate]setupViewControllers:self.navigationController];
        
//        ViewController *calendarView=[[ViewController alloc]initWithNibName:@"ViewController" bundle:nil];
//        [self.navigationController pushViewController:calendarView animated:YES];
    }
}

-(BOOL)checkValidations{
    if (_txtEmailAddress.text && _txtEmailAddress.text.length == 0)
    {
        [[WWCommon getSharedObject]createAlertView:@"Wedding Wise" :@"Please enter email address" :nil :000 ];
        return YES;
    }
    if (_txtPassword.text && _txtPassword.text.length == 0)
    {
        [[WWCommon getSharedObject]createAlertView:@"Wedding Wise" :@"Please enter password" :nil :000 ];
        return NO;
    }
    return YES;
}
-(void)textFieldDidBeginEditing:(UITextField *)textField {
    [self toggleAnimation:textField];
}
- (void)toggleAnimation:(UITextField*)textField {
    
    
}
-(IBAction)btnGoogleLoginPressed:(id)sender{
}
-(void)textFieldDidEndEditing:(UITextField *)textField {
    [self toggleAnimation:textField];
}
- (BOOL)textFieldShouldReturn:(UITextField *)textField{
    if (textField==_txtEmailAddress){
        [self.txtPassword becomeFirstResponder];
    }
    else if(textField==_txtPassword){
        [_txtPassword resignFirstResponder];
    }
    return YES;
}
-(IBAction)btnForgotPasswordPressed:(id)sender{
    WWForgotPassword *forgotPasowrd=[[WWForgotPassword alloc]initWithNibName:@"WWForgotPassword" bundle:nil];
    [self.navigationController pushViewController:forgotPasowrd animated:YES];
}
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
