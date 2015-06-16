package com.wedwise.tab;

import java.util.ArrayList;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.Window;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;

import com.wedwise.adapter.SpinnerAdapter;
import com.wedwiseapp.R;

public class BidBookCreateActivity extends FragmentActivity{

	TextView tvTitle;
	Button btnBitIt;
	Spinner spTimeSlot,spPerPlate,spMinPerson;
	ArrayList<String> listAdapter;
	ArrayList<String> listTimings;
	SpinnerAdapter  adapterSpinner;

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.bid_book_create);
		tvTitle=(TextView) findViewById(R.id.tvTitle);
		btnBitIt=(Button) findViewById(R.id.btnBitIt);

		listAdapter=new ArrayList<String>();
		listAdapter.add("200");
		listAdapter.add("300");
		listAdapter.add("600");
		listTimings=new ArrayList<String>();
		listTimings.add("Morning");
		listTimings.add("Noon");
		listTimings.add("Evening");
		listTimings.add("Night");
		adapterSpinner=new SpinnerAdapter(BidBookCreateActivity.this, listAdapter);
		spTimeSlot=(Spinner) findViewById(R.id.spTimeSlot);
		spPerPlate=(Spinner) findViewById(R.id.spPerPlate);
		spMinPerson=(Spinner) findViewById(R.id.spMinPerson);

		spPerPlate.setAdapter(adapterSpinner);
		spMinPerson.setAdapter(adapterSpinner);

		adapterSpinner=new SpinnerAdapter(BidBookCreateActivity.this, listTimings);
		spTimeSlot.setAdapter(adapterSpinner);
		
		if(getIntent().getExtras().getString("type").equals("bid"))
		{
			tvTitle.setText("Create Bid");
			btnBitIt.setText("BID IT");
		}
		else if(getIntent().getExtras().getString("type").equals("book"))
		{
			tvTitle.setText("Create Book");
			btnBitIt.setText("BOOK IT");
		}
	}
}
