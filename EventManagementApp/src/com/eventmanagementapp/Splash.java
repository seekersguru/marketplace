package com.eventmanagementapp;

import com.eventmanagementapp.calendar.CalendarActivity;
import com.eventmanagementapp.util.PreferenceUtil;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.Window;

public class Splash extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.activity_splash);
		PreferenceUtil.init(this);

	}

	@Override
	protected void onPause() {
		super.onPause();
	}

	@Override
	protected void onResume() {
		super.onResume();
		launch(this);
	}

	private void launch(final Context context) {
		Handler handler = new Handler();
		boolean isRegistered = PreferenceUtil.getInstance().isRegistered();
		if (isRegistered == true) {
			handler.postDelayed(new Runnable() {
				@Override
				public void run() {
					startActivity(new Intent(Splash.this,CalendarActivity.class));
					overridePendingTransition(R.anim.right_in, R.anim.left_out);
					finish();
				}
			}, 2000);

		} else {
			handler.postDelayed(new Runnable() {
				@Override
				public void run() {
					Intent myIntent=new Intent(context,LoginSignUpActivity.class);
					startActivity(myIntent);
					overridePendingTransition(R.anim.right_in, R.anim.left_out);
					finish();
				}
			}, 2000);
		}
	}
}
