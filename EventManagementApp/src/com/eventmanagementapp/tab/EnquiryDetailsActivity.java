package com.eventmanagementapp.tab;

import java.util.ArrayList;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.View;
import android.view.Window;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

import com.eventmanagementapp.R;
import com.eventmanagementapp.adapter.EnquiryDetailsAdapter;
import com.eventmanagementapp.bean.EnquiryDetailsDataBean;

public class EnquiryDetailsActivity extends FragmentActivity implements OnClickListener{

	Button btnBack;
	TextView tvTitle;
	ListView lvPrice;
	Button btnAccept,btnReject,btnNewOffer;
	EnquiryDetailsAdapter adapter;
	ArrayList<EnquiryDetailsDataBean> listData=new ArrayList<EnquiryDetailsDataBean>();

	@Override
	protected void onCreate(Bundle arg0) {
		super.onCreate(arg0);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.enquirydetails);
		btnBack=(Button) findViewById(R.id.btnBack);
		tvTitle=(TextView) findViewById(R.id.tvTitle);
		lvPrice=(ListView) findViewById(R.id.lvPrice);
		btnAccept=(Button) findViewById(R.id.btnAccept);
		btnReject=(Button) findViewById(R.id.btnReject);
		btnNewOffer=(Button) findViewById(R.id.btnNewOffer);
		btnAccept.setOnClickListener(this);
		btnReject.setOnClickListener(this);
		btnNewOffer.setOnClickListener(this);
		btnBack.setOnClickListener(this);

		EnquiryDetailsDataBean enquiryDataBean=new EnquiryDetailsDataBean("Date", "From","Fax","Rate");
		listData.add(enquiryDataBean);
		EnquiryDetailsDataBean enquiryDataBean2=new EnquiryDetailsDataBean("18/6/2015", "Us","350","1800+");
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);
		listData.add(enquiryDataBean2);

		adapter=new EnquiryDetailsAdapter(EnquiryDetailsActivity.this, listData);
		lvPrice.setAdapter(adapter);
	}

	@Override
	public void onClick(View v) {
		switch (v.getId()) {
		case R.id.btnBack:
			finish();		
			overridePendingTransition(R.anim.right_in, R.anim.right_out);
			break;
		case R.id.btnAccept:
			break;
		case R.id.btnReject:
			break;
		case R.id.btnNewOffer:
			break;
		default:
			break;
		}
	}

	@Override
	public void onBackPressed() {
		super.onBackPressed();
		finish();		
		overridePendingTransition(R.anim.right_in, R.anim.right_out);
	}
}
