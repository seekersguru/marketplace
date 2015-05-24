package io.swagger.client.api;

import io.swagger.client.ApiException;
import io.swagger.client.ApiInvoker;

import io.swagger.client.model.*;

import java.util.*;

import io.swagger.client.model.RegisterResponse;

import org.apache.http.HttpEntity;
import org.apache.http.entity.mime.MultipartEntityBuilder;

import java.util.Map;
import java.util.HashMap;
import java.io.File;

public class DefaultApi {
  String basePath = "https://api.wedwise.com/v1";
  ApiInvoker apiInvoker = ApiInvoker.getInstance();

  public void addHeader(String key, String value) {
    getInvoker().addDefaultHeader(key, value);
  }

  public ApiInvoker getInvoker() {
    return apiInvoker;
  }

  public void setBasePath(String basePath) {
    this.basePath = basePath;
  }

  public String getBasePath() {
    return basePath;
  }

  
  /**
   * 
   * 
   * @param firstname First Name (Optional)
   * @param lastname Last Name (Optional)
   * @param email user email address
   * @param password password of user
   * @return RegisterResponse
   */
  public RegisterResponse  registerPost (String firstname, String lastname, String email, String password) throws ApiException {
    Object postBody = null;
    
    // verify the required parameter 'email' is set
    if (email == null) {
       throw new ApiException(400, "Missing the required parameter 'email' when calling registerPost");
    }
    
    // verify the required parameter 'password' is set
    if (password == null) {
       throw new ApiException(400, "Missing the required parameter 'password' when calling registerPost");
    }
    

    // create path and map variables
    String path = "/register".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();

    

    

    String[] contentTypes = {
      
    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder builder = MultipartEntityBuilder.create();
      
      if (firstname != null) {
        builder.addTextBody("firstname", ApiInvoker.parameterToString(firstname), ApiInvoker.TEXT_PLAIN_UTF8);
      }
      
      if (lastname != null) {
        builder.addTextBody("lastname", ApiInvoker.parameterToString(lastname), ApiInvoker.TEXT_PLAIN_UTF8);
      }
      
      if (email != null) {
        builder.addTextBody("email", ApiInvoker.parameterToString(email), ApiInvoker.TEXT_PLAIN_UTF8);
      }
      
      if (password != null) {
        builder.addTextBody("password", ApiInvoker.parameterToString(password), ApiInvoker.TEXT_PLAIN_UTF8);
      }
      

      HttpEntity httpEntity = builder.build();
      postBody = httpEntity;
    } else {
      // normal form params
      formParams.put("firstname", ApiInvoker.parameterToString(firstname));
      formParams.put("lastname", ApiInvoker.parameterToString(lastname));
      formParams.put("email", ApiInvoker.parameterToString(email));
      formParams.put("password", ApiInvoker.parameterToString(password));
      
    }

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "POST", queryParams, postBody, headerParams, formParams, contentType);
      if(response != null){
        return (RegisterResponse) ApiInvoker.deserialize(response, "", RegisterResponse.class);
      }
      else {
        return null;
      }
    } catch (ApiException ex) {
      throw ex;
    }
  }
  
  /**
   * 
   * 
   * @param cid Confirmation uid
   * @return void
   */
  public void  registerConfirmPost (String cid) throws ApiException {
    Object postBody = null;
    
    // verify the required parameter 'cid' is set
    if (cid == null) {
       throw new ApiException(400, "Missing the required parameter 'cid' when calling registerConfirmPost");
    }
    

    // create path and map variables
    String path = "/registerConfirm".replaceAll("\\{format\\}","json");

    // query params
    Map<String, String> queryParams = new HashMap<String, String>();
    // header params
    Map<String, String> headerParams = new HashMap<String, String>();
    // form params
    Map<String, String> formParams = new HashMap<String, String>();

    if (cid != null)
      queryParams.put("cid", ApiInvoker.parameterToString(cid));
    

    

    String[] contentTypes = {
      
    };
    String contentType = contentTypes.length > 0 ? contentTypes[0] : "application/json";

    if (contentType.startsWith("multipart/form-data")) {
      // file uploading
      MultipartEntityBuilder builder = MultipartEntityBuilder.create();
      

      HttpEntity httpEntity = builder.build();
      postBody = httpEntity;
    } else {
      // normal form params
      
    }

    try {
      String response = apiInvoker.invokeAPI(basePath, path, "POST", queryParams, postBody, headerParams, formParams, contentType);
      if(response != null){
        return ;
      }
      else {
        return ;
      }
    } catch (ApiException ex) {
      throw ex;
    }
  }
  
}
