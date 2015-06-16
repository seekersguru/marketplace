package com.wedwiseapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.wedwise.calendar.CalendarActivity;

public class VendorDetailsActivity extends FragmentActivity {

	Button btnBack,btnSchedule;
	TextView tvReadMore;
	ImageView imViewMap;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.vendor_details);
		tvReadMore=(TextView) findViewById(R.id.tvReadMore);
		btnSchedule=(Button) findViewById(R.id.btnSchedule);

		imViewMap=(ImageView) findViewById(R.id.imViewMap);

		imViewMap.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				Intent myIntent=new Intent(VendorDetailsActivity.this,VendorDetailsPageMapPopup.class);
				startActivity(myIntent);	
				overridePendingTransition(R.anim.right_in, R.anim.left_out);				
			}
		});

		btnSchedule.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				Intent myIntent=new Intent(VendorDetailsActivity.this,CalendarActivity.class);
				startActivity(myIntent);	
				overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
		tvReadMore.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
			}
		});
		idInitialization();
	}

	private void idInitialization() {

	}
	@Override
	public void onBackPressed() {
		// TODO Auto-generated method stub
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
