package com.eventmanagementapp.adapter;

import java.util.ArrayList;
import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;
import com.eventmanagementapp.R;
import com.eventmanagementapp.bean.EnquiryDataBean;
import com.eventmanagementapp.bean.EnquiryDetailsDataBean;

public class EnquiryDataAdapter extends BaseAdapter{

	Context mContext;
	public ArrayList<EnquiryDataBean> listEnquiryDataBean=new ArrayList<EnquiryDataBean>();

	public EnquiryDataAdapter(Context mContext,ArrayList<EnquiryDataBean> listEnquiryDataBean)
	{
		this.mContext=mContext;	
		this.listEnquiryDataBean=listEnquiryDataBean;
	}

	@Override
	public int getCount() {
		return listEnquiryDataBean.size();
	}

	@Override
	public Object getItem(int position) {
		return position;
	}

	@Override
	public long getItemId(int position) {
		return position;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		View listItem = convertView;
		LayoutInflater inflater = ((Activity) mContext).getLayoutInflater();
		listItem = inflater.inflate(R.layout.enquiryactivityviewadapter, parent, false);
		TextView tvName=(TextView) listItem.findViewById(R.id.tvName);
		TextView tvDateFirst=(TextView) listItem.findViewById(R.id.tvDateFirst);
		TextView tvDateSecond=(TextView) listItem.findViewById(R.id.tvDateSecond);
		TextView tvPackageDedtails=(TextView) listItem.findViewById(R.id.tvPackageDedtails);

		tvName.setText(listEnquiryDataBean.get(position).getName());
		tvDateFirst.setText(listEnquiryDataBean.get(position).getDateFirst());
		tvDateSecond.setText(listEnquiryDataBean.get(position).getDateSecond());
		tvPackageDedtails.setText(listEnquiryDataBean.get(position).getPackageDetails());
		return listItem;
	}
}
