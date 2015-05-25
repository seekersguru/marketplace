#import "SWGDefaultApi.h"
#import "SWGFile.h"
#import "SWGQueryParamCollection.h"
#import "SWGApiClient.h"
#import "SWGRegisterResponse.h"


@interface SWGDefaultApi ()
    @property (readwrite, nonatomic, strong) NSMutableDictionary *defaultHeaders;
@end

@implementation SWGDefaultApi
static NSString * basePath = @"https://api.wedwise.com/v1";

+(SWGDefaultApi*) apiWithHeader:(NSString*)headerValue key:(NSString*)key {
    static SWGDefaultApi* singletonAPI = nil;

    if (singletonAPI == nil) {
        singletonAPI = [[SWGDefaultApi alloc] init];
        [singletonAPI addHeader:headerValue forKey:key];
    }
    return singletonAPI;
}

+(void) setBasePath:(NSString*)path {
    basePath = path;
}

+(NSString*) getBasePath {
    return basePath;
}

-(SWGApiClient*) apiClient {
    return [SWGApiClient sharedClientFromPool:basePath];
}

-(void) addHeader:(NSString*)value forKey:(NSString*)key {
    [self.defaultHeaders setValue:value forKey:key];
}

-(id) init {
    self = [super init];
    self.defaultHeaders = [NSMutableDictionary dictionary];
    [self apiClient];
    return self;
}

-(void) setHeaderValue:(NSString*) value
           forKey:(NSString*)key {
    [self.defaultHeaders setValue:value forKey:key];
}

-(unsigned long) requestQueueSize {
    return [SWGApiClient requestQueueSize];
}


/*!
 * 
 * 
 * \param firstname First Name (Optional)
 * \param lastname Last Name (Optional)
 * \param email user email address
 * \param password password of user
 * \returns SWGRegisterResponse*
 */
-(NSNumber*) registerPostWithCompletionBlock: (NSString*) firstname
         lastname: (NSString*) lastname
         email: (NSString*) email
         password: (NSString*) password
        
        completionHandler: (void (^)(SWGRegisterResponse* output, NSError* error))completionBlock
         {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/register", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    

    NSArray* requestContentTypes = @[];
    NSString* requestContentType = [requestContentTypes count] > 0 ? requestContentTypes[0] : @"application/json";

    NSArray* responseContentTypes = @[];
    NSString* responseContentType = [responseContentTypes count] > 0 ? responseContentTypes[0] : @"application/json";

    NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    
    NSMutableDictionary* headerParams = [NSMutableDictionary dictionaryWithDictionary:self.defaultHeaders];

    

    id bodyDictionary = nil;
    
    

    NSMutableDictionary * formParams = [[NSMutableDictionary alloc]init];

    
    
    formParams[@"firstname"] = firstname;
    
    if(bodyDictionary == nil) {
      bodyDictionary = [[NSMutableArray alloc] init];
    }
    [bodyDictionary addObject:formParams];
    
    
    formParams[@"lastname"] = lastname;
    
    if(bodyDictionary == nil) {
      bodyDictionary = [[NSMutableArray alloc] init];
    }
    [bodyDictionary addObject:formParams];
    
    
    formParams[@"email"] = email;
    
    if(bodyDictionary == nil) {
      bodyDictionary = [[NSMutableArray alloc] init];
    }
    [bodyDictionary addObject:formParams];
    
    
    formParams[@"password"] = password;
    
    if(bodyDictionary == nil) {
      bodyDictionary = [[NSMutableArray alloc] init];
    }
    [bodyDictionary addObject:formParams];
    
    

    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    
    // non container response

    

    
    // complex response
        
    // comples response type
    return [client dictionary: requestUrl
                       method: @"POST"
                  queryParams: queryParams
                         body: bodyDictionary
                 headerParams: headerParams
           requestContentType: requestContentType
          responseContentType: responseContentType
              completionBlock: ^(NSDictionary *data, NSError *error) {
                if (error) {
                    completionBlock(nil, error);
                    
                    return;
                }
                SWGRegisterResponse* result = nil;
                if (data) {
                    result = [[SWGRegisterResponse  alloc]  initWithDictionary:data error:nil];
                }
                completionBlock(result , nil);
                
              }];
    

    

    
}

/*!
 * 
 * 
 * \param cid Confirmation uid
 * \returns void
 */
-(NSNumber*) registerConfirmPostWithCompletionBlock: (NSString*) cid
        
        
        completionHandler: (void (^)(NSError* error))completionBlock {

    NSMutableString* requestUrl = [NSMutableString stringWithFormat:@"%@/registerConfirm", basePath];

    // remove format in URL if needed
    if ([requestUrl rangeOfString:@".{format}"].location != NSNotFound)
        [requestUrl replaceCharactersInRange: [requestUrl rangeOfString:@".{format}"] withString:@".json"];

    

    NSArray* requestContentTypes = @[];
    NSString* requestContentType = [requestContentTypes count] > 0 ? requestContentTypes[0] : @"application/json";

    NSArray* responseContentTypes = @[];
    NSString* responseContentType = [responseContentTypes count] > 0 ? responseContentTypes[0] : @"application/json";

    NSMutableDictionary* queryParams = [[NSMutableDictionary alloc] init];
    if(cid != nil) {
        
        queryParams[@"cid"] = cid;
    }
    
    NSMutableDictionary* headerParams = [NSMutableDictionary dictionaryWithDictionary:self.defaultHeaders];

    

    id bodyDictionary = nil;
    
    

    NSMutableDictionary * formParams = [[NSMutableDictionary alloc]init];

    
    

    

    SWGApiClient* client = [SWGApiClient sharedClientFromPool:basePath];

    

    

    
    // it's void
        return [client stringWithCompletionBlock: requestUrl 
                                      method: @"POST" 
                                 queryParams: queryParams 
                                        body: bodyDictionary 
                                headerParams: headerParams
                          requestContentType: requestContentType
                         responseContentType: responseContentType
                             completionBlock: ^(NSString *data, NSError *error) {
                if (error) {
                    completionBlock(error);
                    return;
                }
                completionBlock(nil);
                    }];

    
}



@end
