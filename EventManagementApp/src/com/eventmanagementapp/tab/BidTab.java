package com.eventmanagementapp.tab;

import java.util.ArrayList;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

import com.eventmanagementapp.R;
import com.eventmanagementapp.adapter.BookListAdapter;
import com.eventmanagementapp.adapter.EnquiryDataAdapter;
import com.eventmanagementapp.bean.EnquiryDataBean;

/**
 */
public class BidTab extends Fragment {

	ListView lvBid;
	BookListAdapter adapterMessageList;
	//	LinearLayout llFieldsSecond;
	ArrayList<EnquiryDataBean> listEnquiryDataBean=new ArrayList<EnquiryDataBean>();
	EnquiryDataAdapter adapter;

	@Override
	public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
		View v = inflater.inflate(R.layout.bidtab,container,false);
		idInitialization(v);
		return v;
	}

	private void idInitialization(View view)
	{
		lvBid=(ListView) view.findViewById(R.id.lvBid);
		EnquiryDataBean dataobj=new EnquiryDataBean("Gupta & Sharma", "23-Nov-2015","21-Dec-2015","Pax:350-45 Package: NVS Rev:5-5100 Source:Wedwise");
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		listEnquiryDataBean.add(dataobj);
		adapter=new EnquiryDataAdapter(getActivity(),listEnquiryDataBean);
		lvBid.setAdapter(adapter);
		lvBid.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view, int position,
					long id) {
				Intent myIntent=new Intent(getActivity(),EnquiryDetailsActivity.class);
				startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);			
			}
		});		
		/*listMessages.add("Andy Lau");
		listMessages.add("James Moore");
		listMessages.add("Jorgen Flood");
		listMessages.add("Claude");
		listMessages.add("Stefanos Fanidis");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		adapterMessageList=new BookListAdapter(getActivity(), listMessages);
		lvBid.setAdapter(adapterMessageList);
		lvBid.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent=new Intent(getActivity(),BidBookDetailsScreenActivity.class);
				startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
				Intent myIntent=new Intent(getActivity(),MessageChatActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});*/
	}
}