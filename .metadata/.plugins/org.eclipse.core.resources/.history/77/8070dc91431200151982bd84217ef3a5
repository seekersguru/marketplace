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
import com.eventmanagementapp.Activities.MessageChatActivity;
import com.eventmanagementapp.adapter.MessagesListAdapter;

/**
 */
public class Tab3 extends Fragment {

	ListView lvMessages;
	ArrayList<String> listMessages;
	MessagesListAdapter adapterMessageList;

	@Override
	public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
		View v = inflater.inflate(R.layout.tab_3,container,false);
		idInitialization(v);
		return v;
	}

	private void idInitialization(View view)
	{
		lvMessages=(ListView) view.findViewById(R.id.lvMessages);
		listMessages=new ArrayList<String>();
		listMessages.add("Andy Lau");
		listMessages.add("James Moore");
		listMessages.add("Jorgen Flood");
		listMessages.add("Claude");
		listMessages.add("Stefanos Fanidis");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		listMessages.add("James Moore");
		adapterMessageList=new MessagesListAdapter(getActivity(), listMessages);
		lvMessages.setAdapter(adapterMessageList);
		lvMessages.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent=new Intent(getActivity(),MessageChatActivity.class);
				/*getActivity().*/startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});
	}
}