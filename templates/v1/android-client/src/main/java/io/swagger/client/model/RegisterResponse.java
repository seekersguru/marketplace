package io.swagger.client.model;


import com.wordnik.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;


@ApiModel(description = "")
public class RegisterResponse  {
  
  @SerializedName("uid")
  private String uid = null;
  @SerializedName("message")
  private String message = null;
  @SerializedName("userStatus")
  private String userStatus = null;

  
  /**
   * user unique wedwise id
   **/
  @ApiModelProperty(value = "user unique wedwise id")
  public String getUid() {
    return uid;
  }
  public void setUid(String uid) {
    this.uid = uid;
  }

  
  /**
   * message indicates further action need to perform
   **/
  @ApiModelProperty(value = "message indicates further action need to perform")
  public String getMessage() {
    return message;
  }
  public void setMessage(String message) {
    this.message = message;
  }

  
  /**
   * User Status
   **/
  @ApiModelProperty(value = "User Status")
  public String getUserStatus() {
    return userStatus;
  }
  public void setUserStatus(String userStatus) {
    this.userStatus = userStatus;
  }

  

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class RegisterResponse {\n");
    
    sb.append("  uid: ").append(uid).append("\n");
    sb.append("  message: ").append(message).append("\n");
    sb.append("  userStatus: ").append(userStatus).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}
