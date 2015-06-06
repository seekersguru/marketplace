package com.eventmanagementapp;

import android.graphics.Color;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.Toolbar;
import android.text.Editable;
import android.text.Html;
import android.text.TextWatcher;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.eventmanagementapp.util.SystemBarTintManager;

public class RegistrationSignUpActivity extends FragmentActivity implements
TextWatcher{

	EditText  etPassword,etBrideName,etGroomName,etArea;
	Button btnSignIn,btnBack;
	TextView tvToolBar,tvBottomBar;
	Toolbar toolbar;

	//	@Override
	//	public void onWindowFocusChanged(boolean hasFocus) {
	//		super.onWindowFocusChanged(hasFocus);
	//		if (hasFocus) {
	//			getWindow().getDecorView().setSystemUiVisibility(
	//					View.SYSTEM_UI_FLAG_LAYOUT_STABLE
	//					| View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
	//					| View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
	//					| View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
	//					| View.SYSTEM_UI_FLAG_FULLSCREEN
	//					| View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
	//		}
	//	}

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		//		setTheme(android.R.style.Theme_Holo_Light_NoActionBar_TranslucentDecor);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.registration);
		// create our manager instance after the content view is set
		SystemBarTintManager tintManager = new SystemBarTintManager(this);
		// enable status bar tint
		tintManager.setStatusBarTintEnabled(true);
		// enable navigation bar tint
		tintManager.setNavigationBarTintEnabled(true);
		tintManager.setStatusBarAlpha(0.0f);
		tintManager.setNavigationBarAlpha(0.0f);
		toolbar=(Toolbar) findViewById(R.id.toolbar);
		btnBack=(Button) toolbar.findViewById(R.id.btnBack);
		tvToolBar=(TextView)toolbar.findViewById(R.id.tvToolBar);
		tvToolBar.setText("Sign In");
		etPassword=(EditText) findViewById(R.id.etPassword);
		etBrideName=(EditText) findViewById(R.id.etBrideName);
		etGroomName=(EditText) findViewById(R.id.etGroomName);
		etArea=(EditText) findViewById(R.id.etArea);
		tvBottomBar=(TextView) findViewById(R.id.tvBottomBar);
		tvBottomBar.setText(Html.fromHtml("By signing up,I agree to terms of<br>services,privacy policies,guest policies,<br>and host guarantee terms.").toString());
		etPassword.setHintTextColor(Color.parseColor("#5C5858"));
		etBrideName.setHintTextColor(Color.parseColor("#5C5858"));
		etGroomName.setHintTextColor(Color.parseColor("#5C5858"));
		etArea.setHintTextColor(Color.parseColor("#5C5858"));
		btnSignIn=(Button) findViewById(R.id.btnSignIn);
		etPassword.addTextChangedListener(this);
		etBrideName.addTextChangedListener(this);
		etGroomName.addTextChangedListener(this);
		etArea.addTextChangedListener(this);
		btnSignIn.setBackgroundColor(Color.parseColor("#F9B9BA"));
		btnSignIn.setEnabled(false);
		btnBack.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				finish();	
				overridePendingTransition(R.anim.right_in, R.anim.right_out);
			}
		});
		btnSignIn.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {

			}
		});
	}

	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}

	@Override
	public void beforeTextChanged(CharSequence s, int start, int count,
			int after) {
	}

	@Override
	public void onTextChanged(CharSequence s, int start, int before, int count) {
	}

	@Override
	public void afterTextChanged(Editable s) {
		if(etPassword.getText().toString().trim().equals("") || etBrideName.getText().toString().trim().equals("") 
				|| etGroomName.getText().toString().trim().equals("") || etArea.getText().toString().trim().equals(""))
		{
			btnSignIn.setEnabled(false);
			btnSignIn.setBackgroundColor(Color.parseColor("#F9B9BA"));
		}
		else if(!etPassword.getText().toString().trim().equals("") && !etBrideName.getText().toString().trim().equals("") 
				&& !etGroomName.getText().toString().trim().equals("") && !etArea.getText().toString().trim().equals(""))
		{
			btnSignIn.setEnabled(true);
			btnSignIn.setBackgroundColor(Color.parseColor("#E4484B"));
		}		
	}
}
