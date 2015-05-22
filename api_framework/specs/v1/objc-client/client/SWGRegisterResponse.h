#import <Foundation/Foundation.h>
#import "SWGObject.h"


@protocol SWGRegisterResponse
@end
  
@interface SWGRegisterResponse : SWGObject

/* user unique wedwise id [optional]
 */
@property(nonatomic) NSString* uid;
/* message indicates further action need to perform [optional]
 */
@property(nonatomic) NSString* message;
/* User Status [optional]
 */
@property(nonatomic) NSString* userStatus;

@end
