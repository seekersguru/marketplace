package com.wedwiseapp.login;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.Toolbar;
import android.text.Html;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.TextView;

import com.example.wedwiseapp.R;

public class RegisterActivity extends FragmentActivity {
	Button btnFBLogin,btnGoogleLogin,btnSignUp,btnLogin;
	TextView tvBottomBar,tvToolBar;
	Toolbar toolbar;
	Context mContext;

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		setTheme(android.R.style.Theme_Holo_Light_NoActionBar_TranslucentDecor);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		mContext=RegisterActivity.this;
		setContentView(R.layout.loginsignupactivity);
		btnLogin=(Button) findViewById(R.id.btnLogin);
		btnFBLogin=(Button) findViewById(R.id.btnFBLogin);
		btnGoogleLogin=(Button) findViewById(R.id.btnGoogleLogin);
		btnSignUp=(Button) findViewById(R.id.btnSignUp);
		tvBottomBar=(TextView) findViewById(R.id.tvBottomBar);
		tvBottomBar.setText(Html.fromHtml("By signing up,I agree to terms of services,privacy policies,guest policies,and host guarantee terms.").toString());
		toolbar=(Toolbar) findViewById(R.id.toolbar);
		tvToolBar=(TextView)toolbar.findViewById(R.id.tvToolBar);
		tvToolBar.setText("Log In or Sign Up");
		btnSignUp.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent=new Intent(RegisterActivity.this, SignUpActivity.class);
				myIntent.putExtra("type","registration");
				startActivity(myIntent);	
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
		btnLogin.setOnClickListener(new OnClickListener(){
			@Override
			public void onClick(View v) {
				Intent myIntent=new Intent(RegisterActivity.this, SignUpActivity.class);
				myIntent.putExtra("type","login");
				startActivity(myIntent);
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

	}

	@Override
	protected void onStart() {
		super.onStart();
	}

	@Override
	protected void onStop() {
		super.onStop();
	}

	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
