package dao;

import entity.inhosHQMSStandardTemp;

public interface inhosHQMSStandardTempMapper {
    int deleteByPrimaryKey(String id);

    int insert(inhosHQMSStandardTemp record);

    int insertSelective(inhosHQMSStandardTemp record);

    inhosHQMSStandardTemp selectByPrimaryKey(String id);

    int updateByPrimaryKeySelective(inhosHQMSStandardTemp record);

    int updateByPrimaryKey(inhosHQMSStandardTemp record);
}