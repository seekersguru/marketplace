#import "SWGRegisterResponse.h"

@implementation SWGRegisterResponse
  
+ (JSONKeyMapper *)keyMapper
{
  return [[JSONKeyMapper alloc] initWithDictionary:@{ @"uid": @"uid", @"message": @"message", @"userStatus": @"userStatus" }];
}

+ (BOOL)propertyIsOptional:(NSString *)propertyName
{
  NSArray *optionalProperties = @[@"uid", @"message", @"userStatus"];

  if ([optionalProperties containsObject:propertyName]) {
    return YES;
  }
  else {
    return NO;
  }
}

@end
