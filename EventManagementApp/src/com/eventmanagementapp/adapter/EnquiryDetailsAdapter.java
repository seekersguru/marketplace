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
import com.eventmanagementapp.bean.EnquiryDetailsDataBean;

public class EnquiryDetailsAdapter extends BaseAdapter{

	Context mContext;
	public ArrayList<EnquiryDetailsDataBean> listData=new ArrayList<EnquiryDetailsDataBean>();

	public EnquiryDetailsAdapter(Context mContext,ArrayList<EnquiryDetailsDataBean> listData)
	{
		this.mContext=mContext;	
		this.listData=listData;
	}

	@Override
	public int getCount() {
		return listData.size();
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
		listItem = inflater.inflate(R.layout.enquirydetailsadapter, parent, false);
		TextView tvDate=(TextView) listItem.findViewById(R.id.tvDate);
		TextView tvFrom=(TextView) listItem.findViewById(R.id.tvFrom);
		TextView tvFax=(TextView) listItem.findViewById(R.id.tvFax);
		TextView tvRate=(TextView) listItem.findViewById(R.id.tvRate);

		tvDate.setText(listData.get(position).getDate());
		tvFrom.setText(listData.get(position).getFrom());
		tvFax.setText(listData.get(position).getFax());
		tvRate.setText(listData.get(position).getRate());
		return listItem;
	}
}
