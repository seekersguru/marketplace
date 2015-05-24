#import <Foundation/Foundation.h>
#import "SWGRegisterResponse.h"
#import "SWGObject.h"


@interface SWGDefaultApi: NSObject

-(void) addHeader:(NSString*)value forKey:(NSString*)key;
-(unsigned long) requestQueueSize;
+(SWGDefaultApi*) apiWithHeader:(NSString*)headerValue key:(NSString*)key;
+(void) setBasePath:(NSString*)basePath;
+(NSString*) getBasePath;
/**

 
 

 @param firstname First Name (Optional)
 @param lastname Last Name (Optional)
 @param email user email address
 @param password password of user
 

 return type: SWGRegisterResponse*
 */
-(NSNumber*) registerPostWithCompletionBlock :(NSString*) firstname 
     lastname:(NSString*) lastname 
     email:(NSString*) email 
     password:(NSString*) password 
    
    completionHandler: (void (^)(SWGRegisterResponse* output, NSError* error))completionBlock;
    


/**

 
 

 @param cid Confirmation uid
 

 return type: 
 */
-(NSNumber*) registerConfirmPostWithCompletionBlock :(NSString*) cid 
    
    
    completionHandler: (void (^)(NSError* error))completionBlock;



@end