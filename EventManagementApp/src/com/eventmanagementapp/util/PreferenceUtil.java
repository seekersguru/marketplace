package com.eventmanagementapp.util;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Build;
import android.preference.PreferenceManager;

public class PreferenceUtil {

	private SharedPreferences sp;
	private SharedPreferences.Editor editor;	
	private static PreferenceUtil instance;

	private PreferenceUtil(Context context) {
		sp = PreferenceManager.getDefaultSharedPreferences(context);
		editor = sp.edit();
	}
	
	public static void init(Context context) {
		instance = new PreferenceUtil(context);
	}
	
	public static PreferenceUtil getInstance(){
		return instance;
	}

	public boolean getWifiMode() {
		boolean wifiMode;
		if (Build.VERSION.SDK_INT < Build.VERSION_CODES.ICE_CREAM_SANDWICH) {
			wifiMode = sp.getBoolean("checkWifiMode", false);
		} else {
			wifiMode = sp.getBoolean("switchWifiMode", false);
		}
		return wifiMode;
	}

	public Boolean isRegistered() {
		Boolean isRegistered = sp.getBoolean("isRegistered", false);
		return isRegistered;
	}

	public void setRegister(boolean value) {
		editor.putBoolean("isRegistered", value);
		editor.commit();
	}
	
	public String getUid() {
		String uid = sp.getString("uid", null);
		return uid;
	}
	
	public void setUid(String uid) {
		editor.putString("uid", uid);
		editor.commit();
	}
}
