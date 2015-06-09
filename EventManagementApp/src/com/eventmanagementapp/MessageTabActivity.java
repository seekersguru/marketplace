package com.eventmanagementapp;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.support.v4.view.ViewPager;
import android.support.v7.app.ActionBarActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;

import com.eventmanagementapp.tab.SlidingTabLayout;
import com.eventmanagementapp.tab.ViewPagerAdapter;
import com.eventmanagementapp.util.SystemBarTintManager;


public class MessageTabActivity extends ActionBarActivity{

	Context mContext;
	Toolbar toolbar;
	Button btnBack;

	//	Toolbar toolbar;
	ViewPager pager;
	ViewPagerAdapter adapter;
	SlidingTabLayout tabs;
	CharSequence Titles[]={"Bid","Book","Message"};
	int Numboftabs =3;

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
//		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.messagetabactivity);	
		mContext=MessageTabActivity.this;
		/*// create our manager instance after the content view is set
		SystemBarTintManager tintManager = new SystemBarTintManager(this);
		// enable status bar tint
		tintManager.setStatusBarTintEnabled(true);
		// enable navigation bar tint
		tintManager.setNavigationBarTintEnabled(true);
		tintManager.setStatusBarAlpha(0.0f);
		tintManager.setNavigationBarAlpha(0.0f);*/
		toolbar=(Toolbar) findViewById(R.id.toolbar);
//		btnBack=(Button) toolbar.findViewById(R.id.btnBack);
//		btnBack=(Button) toolbar.findViewById(R.id.btnBack);
//		btnBack.setBackgroundResource(R.drawable.arrow_back_orange);
//		btnBack.setOnClickListener(new OnClickListener() {
//			@Override
//			public void onClick(View v) {
//				finish();	
//				overridePendingTransition(R.anim.right_in, R.anim.right_out);
//			}
//		});



		// Creating The Toolbar and setting it as the Toolbar for the activity

		toolbar = (Toolbar) findViewById(R.id.toolbar);
//		toolbar.setVisibility(View.GONE);
		setSupportActionBar(toolbar);


		// Creating The ViewPagerAdapter and Passing Fragment Manager, Titles fot the Tabs and Number Of Tabs.
		adapter =  new ViewPagerAdapter(getSupportFragmentManager(),Titles,Numboftabs);

		// Assigning ViewPager View and setting the adapter
		pager = (ViewPager) findViewById(R.id.pager);
		pager.setAdapter(adapter);

		// Assiging the Sliding Tab Layout View
		tabs = (SlidingTabLayout) findViewById(R.id.tabs);
		tabs.setDistributeEvenly(true); // To make the Tabs Fixed set this true, This makes the tabs Space Evenly in Available width

		// Setting Custom Color for the Scroll bar indicator of the Tab View
		tabs.setCustomTabColorizer(new SlidingTabLayout.TabColorizer() {
			@Override
			public int getIndicatorColor(int position) {
				return getResources().getColor(R.color.tabsScrollColor);
			}
		});



	}
	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
