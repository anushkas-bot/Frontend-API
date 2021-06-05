import React, {useEffect, useState} from "react";
import { Container, Row, Col } from "shards-react";

import PageTitle from "../components/common/PageTitle";
import Editor from "../components/add-new-post/Editor";
import SidebarActions from "../components/add-new-post/SidebarActions";
import SidebarCategories from "../components/add-new-post/SidebarCategories";

var formdata = new FormData();
formdata.append("Title", "gunjan");
formdata.append("Content", "gunjan");
formdata.append("Img", "/C:/Users/parth/Pictures/1600328497491.jpg");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://localhost:8080/api/create/blog", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));

const AddNewPost = ({ smallStats }) => {
  const [data,setData] = useState([])
  useEffect( () => {
    fetch("http://127.0.0.1:5000/lang")
    .then(res =>  res.json())
    .then( res => {setData(res)} )
    console.log('data')
    console.log(data)
  }, [] )

  return (
    <Container fluid className="main-content-container px-4 pb-4">
      {/* Page Header */}
      {
      data.map((data,i) => {
      return (
      <Row noGutters className="page-header py-4">
        <PageTitle style = {{marginTop: 0}} sm={data.sm} title={data.title2} subtitle={data.subtitle2} className="text-sm-left" />
      </Row>
    )
   })
    }
      <Row>
        {/* Editor */}
        <Col style = {{marginTop: 0}} lg="9" md="12">
          <Editor />
        </Col>

        {/* Sidebar Widgets */}
        <Col style = {{marginTop: 0}} lg="3" md="12">
          <SidebarActions style = {{marginTop: 0}} />
          <SidebarCategories style = {{marginTop: 0}} />
        </Col>
      </Row>
    </Container>
  )
};

export default AddNewPost;
