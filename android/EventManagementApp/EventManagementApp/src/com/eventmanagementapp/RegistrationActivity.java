package com.eventmanagementapp;

import android.graphics.Color;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;

public class RegistrationActivity extends FragmentActivity{

	EditText  etEmailAddress,etPassword,etFirstName,etLastName;
	Button btnSignUp;

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.registration);
		etEmailAddress=(EditText) findViewById(R.id.etEmailAddress);
		etPassword=(EditText) findViewById(R.id.etPassword);
		etFirstName=(EditText) findViewById(R.id.etFirstName);
		etLastName=(EditText) findViewById(R.id.etLastName);
		etEmailAddress.setHintTextColor(Color.parseColor("#ffffff"));
		etPassword.setHintTextColor(Color.parseColor("#ffffff"));
		etFirstName.setHintTextColor(Color.parseColor("#ffffff"));
		etLastName.setHintTextColor(Color.parseColor("#ffffff"));
		btnSignUp=(Button) findViewById(R.id.btnSignUp);
		btnSignUp.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub

			}
		});
	}
}
