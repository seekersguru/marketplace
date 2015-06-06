package com.eventmanagementapp.calendar;

import java.util.ArrayList;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;

import com.eventmanagementapp.R;

/**
 * Shows off the most basic usage
 */
public class CalendarActivity extends FragmentActivity implements OnClickListener
{

	MFCalendarView mf;
	Button btnBack,btnAdd,btnCalendar,btnMessage,btnBid,btnMenu;
	Button btnBidTopbar;

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
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setTheme(android.R.style.Theme_Holo_Light_NoActionBar_Fullscreen);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.calendar_activity);

		mf = (MFCalendarView) findViewById(R.id.mFCalendarView);
		btnBack=(Button) findViewById(R.id.btnBack);
		btnBidTopbar=(Button) findViewById(R.id.btnBidTopbar);
		btnAdd=(Button) findViewById(R.id.btnAdd);
		btnCalendar=(Button) findViewById(R.id.btnCalendar);
		btnMessage=(Button) findViewById(R.id.btnMessage);
		btnBid=(Button) findViewById(R.id.btnBid);
		btnMenu=(Button) findViewById(R.id.btnMenu);
		btnBack.setOnClickListener(this);
		btnCalendar.setOnClickListener(this);
		btnMessage.setOnClickListener(this);
		btnBid.setOnClickListener(this);
		btnMenu.setOnClickListener(this);
		/*btnCalendar.setSelected(true);
		btnMessage.setFocusable(false);
		btnBid.setSelected(false);
		btnMenu.setSelected(false);*/
		btnCalendar.performClick();

		mf.setOnCalendarViewListener(new onMFCalendarViewListener() {

			@Override
			public void onDisplayedMonthChanged(int month, int year, String monthStr) {

				StringBuffer bf = new StringBuffer()
				.append(" month:")
				.append(month)
				.append(" year:")
				.append(year)
				.append(" monthStr: ")
				.append(monthStr);
				//				
				//				Toast.makeText(CalendarActivity.this,  bf.toString(),
				//						Toast.LENGTH_SHORT).show();
				//				
			}

			@Override
			public void onDateChanged(String date) {

				//				Toast.makeText(CalendarActivity.this, "onDateChanged:" + date, 
				//						Toast.LENGTH_SHORT).show();
			}
		});

		/**
		 * you can set calendar date anytime
		 * */
		//mf.setDate("2014-02-19");


		/**
		 * calendar events samples 
		 * */
		ArrayList<String> eventDays = new ArrayList<String>();
		eventDays.add("2014-02-25");
		eventDays.add(Util.getTomorrow());
		eventDays.add(Util.getCurrentDate());


		mf.setEvents(eventDays);

		Log.e("","locale:" + Util.getLocale());
	}


	@Override
	public void onBackPressed() {
		super.onBackPressed();
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}

	@Override
	public void onClick(View v) {
		if(v.getId()==R.id.btnBack)
		{
			finish();	
			overridePendingTransition(R.anim.right_in, R.anim.right_out);
		}
		else if(v.getId()==R.id.btnCalendar)
		{
			btnMessage.setSelected(false);
			btnBid.setSelected(false);
			btnMenu.setSelected(false);
			btnCalendar.setSelected(true);
		}
		else if(v.getId()==R.id.btnMessage)
		{
			btnCalendar.setSelected(false);
			btnBid.setSelected(false);
			btnMenu.setSelected(false);
			btnMessage.setSelected(true);
		}
		else if(v.getId()==R.id.btnBid)
		{
			btnCalendar.setSelected(false);
			btnMessage.setSelected(false);
			btnMenu.setSelected(false);
			btnBid.setSelected(true);
		}
		else if(v.getId()==R.id.btnMenu)
		{
			btnCalendar.setSelected(false);
			btnMessage.setSelected(false);
			btnBid.setSelected(false);
			btnMenu.setSelected(true);
		}
	}
}                                                   
/*public class CalendarActivity extends FragmentActivity{

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		setTheme(android.R.style.Theme_Holo_Light_NoActionBar_TranslucentDecor);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.calendar_activity);

	}*/
//}