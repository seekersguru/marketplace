package com.wedwise.fragments;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;

import org.json.JSONArray;
import org.json.JSONObject;

import android.annotation.SuppressLint;
import android.app.Fragment;
import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.DisplayMetrics;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;

import com.wedwise.adapter.AlbumAdapter;
import com.wedwise.common.GlobalCommonMethods;
import com.wedwise.common.GlobalCommonValues;
import com.wedwise.dialogs.ErrorDialog;
import com.wedwise.tab.MessageTabActivity;
import com.wedwiseapp.FavListActivity;
import com.wedwiseapp.R;
import com.wedwiseapp.login.LoginSignUpActivity;
import com.wedwiseapp.util.PreferenceUtil;
import com.wedwiseapp.util.ShowDialog;

public class VendorCategoryHomeFragment extends Fragment{

	ListView lvAlbums;
	AlbumAdapter adapterAlbum;
	ArrayList<HashMap<String,String>> listItems;
	Button btnHome, btnMenu;
	Context mContext;
	String image_type="";
	String response="",url="";
	ProgressDialog progress;

	@Override
	public View onCreateView(LayoutInflater inflater, ViewGroup container,
			Bundle savedInstanceState) {
		View rootView = inflater.inflate(R.layout.vendorcategoryhome, container, false);
		mContext = getActivity();
		idInitialization(rootView);
		return rootView;
	}

	private void idInitialization(View rootView)
	{
		lvAlbums = (ListView)rootView.findViewById(R.id.lvAlbums);
		btnHome = (Button)rootView.findViewById(R.id.btnMail);
		btnMenu = (Button)rootView.findViewById(R.id.btnMenu);

		listItems = new ArrayList<HashMap<String,String>>();
		checkInternetConnection();
		btnMenu.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				boolean isLogin = PreferenceUtil.getInstance().isLogin();
				if(isLogin)
				{
					ErrorDialog dialog=new ErrorDialog();
					dialog.setCancelable(false);
					dialog.newInstance(getActivity(),"Alert!", "You are already logged in",null);
					dialog.show(getFragmentManager(),"tests");
				}
				else if (!isLogin)
				{
					Intent myIntent = new Intent(getActivity(),
							LoginSignUpActivity.class);
					getActivity().startActivity(myIntent);
					getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
				}
				/*Intent myIntent = new Intent(getActivity(),
						LoginSignUpActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);*/
			}
		});

		btnHome.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				Intent myIntent = new Intent(getActivity(),
						MessageTabActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

		adapterAlbum = new AlbumAdapter(mContext, listItems);
		lvAlbums.setAdapter(adapterAlbum);

		lvAlbums.setOnItemClickListener(new OnItemClickListener() {

			@Override
			public void onItemClick(AdapterView<?> parent, View view,
					int position, long id) {
				Intent myIntent = new Intent(getActivity(),
						FavListActivity.class);
				getActivity().startActivity(myIntent);
				getActivity().overridePendingTransition(R.anim.right_in, R.anim.left_out);
			}
		});

	}
	
	@Override
	public void onDestroy() {
		super.onDestroy();
		AlbumAdapter.AnimateFirstDisplayListener.displayedImages.clear();
	}

	private void checkInternetConnection()
	{
		if(GlobalCommonMethods.isNetworkAvailable(mContext))
		{
			url=GlobalCommonValues.CUSTOMER_VENDOR_CATEGORY_HOME;
			new HttpAsyncTask().execute(url);
		}
		else{
			ShowDialog.displayDialog(mContext,"Connection error:","No Internet Connection");
		}
	}

	private class HttpAsyncTask extends AsyncTask<String, Void, Void> {
		@Override
		protected void onPreExecute() {
			super.onPreExecute();
			if(progress==null)
			{
				progress=new ProgressDialog(mContext);
				progress.show();		
			}
		}

		@Override
		protected Void doInBackground(String... params) {
			try {
				// Calling method for setting to be sent to the server
				SetData();
			} catch (Exception e) {
				e.printStackTrace();
			}
			return null;
		}
		// onPostExecute displays the results of the AsyncTask.
		@SuppressLint("DefaultLocale")
		@Override
		protected void onPostExecute(Void result) {
			//			Toast.makeText(getBaseContext(), "Data Sent!"+response, Toast.LENGTH_LONG).show();
			if(progress!=null && progress.isShowing())
			{
				progress.dismiss();
				progress=null;
			}

			if(!TextUtils.isEmpty(response) && GlobalCommonMethods.isJSONValid(response))
			{
				try {
					JSONObject jsonObj = new JSONObject(response);
					JSONArray jsonArray=new JSONObject(jsonObj.getString("json")).getJSONArray("data");
					HashMap<String,String> item;
					for (int i = 0; i < jsonArray.length(); i++)
					{
						item=new HashMap<String, String>();
						String itemFirst=String.valueOf(jsonArray.get(i));
						String[] array=itemFirst.split(",");
						String name=array[0].substring(array[0].indexOf("\"")+1,array[0].lastIndexOf("\"")-1);
						String image_path=array[1].substring(1,array[1].length()-2).replace("\\","");
						item.put("name",name);
						item.put("image_path",image_path);
						listItems.add(item);
					}
					adapterAlbum.listItems=listItems;
					adapterAlbum.notifyDataSetChanged();

				} catch (Exception e) {
					e.getMessage();
				}

			}
		}
	}

	// Create GetData Metod
	public  void  SetData()  throws  UnsupportedEncodingException
	{
		// Create data variable for sent values to server  
		String data="";
		int density = getResources().getDisplayMetrics().densityDpi;

		if(density==DisplayMetrics.DENSITY_MEDIUM)
		{
			image_type="drawable-hdpi";
		}
		else if(density==DisplayMetrics.DENSITY_HIGH)
		{
			image_type="drawable-xhdpi";
		}
		else if(density==DisplayMetrics.DENSITY_XHIGH)
		{
			image_type="drawable-xhdpi";
		}
		else if(density==DisplayMetrics.DENSITY_XXHIGH)
		{
			image_type="drawable-xxhdpi";
		}
		else if(density==DisplayMetrics.DENSITY_XXXHIGH)
		{
			image_type="drawable-xxxhdpi";
		}

		data= URLEncoder.encode("mode", "UTF-8") 
				+ "=" + URLEncoder.encode("android", "UTF-8"); 

		data += "&" + URLEncoder.encode("image_type", "UTF-8") + "="
				+ URLEncoder.encode(image_type, "UTF-8"); 

		BufferedReader reader=null;

		// Send data 
		try
		{ 
			URL _url=null;
			// Defined URL  where to send data
			_url= new URL(GlobalCommonValues.CUSTOMER_VENDOR_CATEGORY_HOME);
			// Send POST data request
			URLConnection conn = _url.openConnection(); 
			conn.setDoOutput(true); 
			OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream()); 
			wr.write( data ); 
			wr.flush(); 

			// Get the server response 
			reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			StringBuilder sb = new StringBuilder();
			String line = null;

			// Read Server Response
			while((line = reader.readLine()) != null)
			{
				// Append server response in string
				sb.append(line + "\n");
			}
			response = sb.toString();
		}
		catch(Exception ex)
		{
		}
		finally
		{
			try
			{
				reader.close();
			}
			catch(Exception ex) {}
		}
	}


}
